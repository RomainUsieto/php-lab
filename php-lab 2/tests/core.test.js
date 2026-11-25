import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {spawnSync} from 'node:child_process';
import {shuffle,exactAnswer,makeSession,sessionScore,selectQuestions,remainingSeconds,isAnswered} from '../js/quiz.js';
import {generateExam, EXAM_CHAPTERS, hasExamComposition} from '../js/exam.js';
import {freshState,validateState,recordAttempt,archiveSession,loadState,saveState} from '../js/storage.js';
import {stats} from '../js/statistics.js';
const bank=[1,2,3,4].flatMap(i=>JSON.parse(readFileSync(new URL(`../data/chapitre-${i}.json`,import.meta.url))));
const byId=new Map(bank.map(q=>[q.id,q]));
test('260 questions documentées, uniques et complètes',()=>{assert.equal(bank.length,260);assert.equal(byId.size,260);assert.equal(new Set(bank.map(q=>q.prompt)).size,260);for(let ch=1;ch<=4;ch++){const qs=bank.filter(q=>q.chapter===ch);assert.equal(qs.filter(q=>q.type==='code').length,15);assert.equal(qs.filter(q=>q.type!=='code').length,50);}for(const q of bank){assert.ok(q.prompt&&q.theme&&q.explanation&&q.answer.length);assert.ok(['facile','intermediaire','difficile'].includes(q.difficulty));assert.ok(q.slides.length&&q.slides.every(n=>n>0&&n<=[48,32,34,50][q.chapter-1]));if(q.type==='code'){assert.equal(q.validation,'self');assert.equal(q.rubric.length,3);assert.ok(q.hint&&q.lineExplanation.length&&q.commonErrors.length);assert.ok(q.answer.split('\n').length<=10);}else{assert.ok(q.options.length>=2);assert.ok(q.options.every(o=>o.explanation));assert.ok(q.answer.every(id=>q.options.some(o=>o.id===id)));assert.ok(q.type==='multiple'?q.answer.length>1:q.answer.length===1);}}});
test('500 examens : chapitres 2 et 3 uniquement, 10 QCM et 2 codes chacun',()=>{let last='';for(let n=0;n<500;n++){const s=generateExam(bank,{duration:45});assert.equal(s.items.length,24);assert.equal(s.immediate,false);assert.equal(new Set(s.items.map(x=>x.id)).size,24);assert.deepEqual(s.examChapters,[2,3]);assert.ok(s.items.every(i=>[2,3].includes(byId.get(i.id).chapter)));for(const c of EXAM_CHAPTERS){const qs=s.items.map(i=>byId.get(i.id)).filter(q=>q.chapter===c);assert.equal(qs.filter(q=>q.type==='code').length,2);assert.equal(qs.filter(q=>q.type!=='code').length,10);}const signature=s.items.map(i=>i.id).join();assert.notEqual(signature,last);last=signature;}});
test('mélange sans mutation, toutes les positions accessibles',()=>{const original=['a','b','c','d'],copy=[...original],positions=new Set();for(let i=0;i<200;i++){const mixed=shuffle(original);assert.deepEqual([...mixed].sort(),copy);positions.add(mixed.indexOf('a'));}assert.deepEqual(original,copy);assert.equal(positions.size,4);});
test('réponses multiples : ordre libre, omissions, surplus et doublons refusés',()=>{const q=bank.find(q=>q.type==='multiple');assert.ok(exactAnswer(q,[...q.answer].reverse()));assert.equal(exactAnswer(q,q.answer.slice(1)),false);assert.equal(exactAnswer(q,[...q.answer,q.options.find(o=>!q.answer.includes(o.id)).id]),false);assert.equal(exactAnswer(q,[q.answer[0],q.answer[0]]),false);});
test('barème pondéré et code provisoire puis final',()=>{const s=generateExam(bank,{weights:{qcm:2,code:10}});for(const {id}of s.items){const q=byId.get(id);if(q.type!=='code')s.answers[id]=q.answer;}let r=sessionScore(s,byId);assert.equal(r.maximum,80);assert.equal(r.pending,4);assert.equal(r.score,10);for(const {id}of s.items)if(byId.get(id).type==='code')s.grades[id]=.5;r=sessionScore(s,byId);assert.equal(r.score,15);assert.equal(r.pending,0);for(const {id}of s.items)if(byId.get(id).type==='code')s.grades[id]=1;assert.equal(sessionScore(s,byId).score,20);});
test('filtrage chapitre, niveau et code, sélection vide',()=>{const cfg={chapters:[2],difficulty:'facile',type:'all',onlyCode:true};const selected=selectQuestions(bank,cfg);assert.ok(selected.length);assert.ok(selected.every(q=>q.chapter===2&&q.difficulty==='facile'&&q.type==='code'));assert.equal(selectQuestions(bank,{...cfg,chapters:[]}).length,0);assert.throws(()=>makeSession([]));});
test('maîtrise après trois succès, sans double comptage',()=>{const state=freshState(),q=bank[0];let s=makeSession([q]);recordAttempt(state,s,q,false);recordAttempt(state,s,q,true);assert.equal(state.progress[q.id].attempts,1);assert.equal(stats(bank,state).errors.length,1);for(let i=0;i<3;i++){s=makeSession([q]);recordAttempt(state,s,q,true);}assert.equal(state.progress[q.id].streak,3);assert.equal(stats(bank,state).errors.length,0);assert.equal(stats(bank,state).mastered,1);assert.equal(stats(bank,state).done,1);});
test('restauration : réponses, ordre mélangé, code, marque et heure préservés',()=>{const state=freshState(),s=generateExam(bank,{duration:30});state.current=s;const code=s.items.find(i=>byId.get(i.id).type==='code');s.answers[code.id]='$x = "  Anna  ";\n';const qcm=s.items.find(i=>byId.get(i.id).type!=='code');s.answers[qcm.id]=[qcm.order[0]];s.marked=[qcm.id];s.index=5;state.favorites=[qcm.id];assert.deepEqual(validateState(JSON.parse(JSON.stringify(state)),byId),state);let saved;globalThis.localStorage={getItem:()=>saved,setItem:(k,v)=>{saved=v;}};assert.equal(saveState(state),true);assert.deepEqual(loadState(byId),state);});
test('imports incohérents refusés, propriétés étrangères sans effet',()=>{assert.throws(()=>validateState({},byId));const state=freshState();state.progress[bank[0].id]={attempts:1,correct:3,wrong:0,streak:3};assert.throws(()=>validateState(state,byId));const invalid=freshState();invalid.current=generateExam(bank);invalid.current.items.pop();assert.throws(()=>validateState(invalid,byId));const parsed=JSON.parse('{"version":1,"progress":{},"favorites":[],"history":[],"prefs":{},"__proto__":{"polluted":true}}');validateState(parsed,byId);assert.equal({}.polluted,undefined);});
test('horloge absolue et expiration',()=>{const s=makeSession([bank[0]],{duration:2});s.startedAt=100000;assert.equal(remainingSeconds(s,130000),90);assert.equal(remainingSeconds(s,250000),0);});
test('historique sans doublon, moyennes hors copies incomplètes',()=>{const state=freshState(),s=generateExam(bank);s.status='submitted';s.submittedAt=Date.now();archiveSession(state,s);archiveSession(state,s);assert.equal(state.history.length,1);assert.equal(stats(bank,state).average,null);for(const i of s.items){const q=byId.get(i.id);if(q.type==='code')s.grades[i.id]=1;else s.answers[i.id]=q.answer;}archiveSession(state,s);assert.equal(stats(bank,state).average,20);assert.equal(stats(bank,state).examCount,1);});
test('code libre : pas de comparaison arbitraire de format',()=>{const q=bank.find(q=>q.type==='code');assert.equal(isAnswered(q,' \n\t '),false);assert.equal(isAnswered(q,"$nom='Anna';\n$age=20;"),true);assert.equal(q.validation,'self');});
test('60 corrections et variantes vérifiées par php -l',()=>{for(const q of bank.filter(q=>q.type==='code'))for(const answer of [q.answer,...q.alternatives]){let code=answer;if(/^(public|private|protected)\b/m.test(code)&&!/^class\s/m.test(code))code=`class TestParent { public function __construct(...$args) {} public function afficherInfos() {} }\nclass TestSolution extends TestParent {\n${code}\n}`;else if(code.includes('$this')&&!/^class\s/m.test(code))code=`class TestSolution {public function test() {\n${code}\n}}`;const result=spawnSync('php',['-l'],{input:'<?php\n'+code,encoding:'utf8'});assert.equal(result.status,0,`${q.id}: ${result.stdout} ${result.stderr}`);}});
test('prédictions exécutées sur le vrai PHP local',()=>{for(const [code,expected] of [['$nom="Anna";echo "Bonjour ".$nom;','Bonjour Anna'],['for($i=0;$i<3;$i++){echo $i;}','012'],['$i=6;while($i<=5){echo $i;$i++;}',''],['function f($a,$b){return $a+$b;}echo f(5,3);','8'],['echo (12+15+9)/3;','12'],['echo (20 === "20") ? "vrai" : "faux";','faux']]){const result=spawnSync('php',[],{input:'<?php '+code,encoding:'utf8'});assert.equal(result.status,0);assert.equal(result.stdout,expected);}});
test('un tirage identique à la copie précédente est remplacé',()=>{const random=Math.random;try{Math.random=()=>.5;const previous=generateExam(bank),next=generateExam(bank,{previousIds:previous.items.map(i=>i.id)});assert.notDeepEqual(previous.items.map(i=>i.id).sort(),next.items.map(i=>i.id).sort());}finally{Math.random=random;}});
test('le périmètre 2–3 reste imposé même si une configuration propose d’autres chapitres',()=>{
  const s=generateExam(bank,{chapters:[1,4]});
  assert.ok(hasExamComposition(s.items,byId,[2,3]));
  assert.equal(hasExamComposition(s.items,byId,[1,2,3,4]),false);
  const restored=validateState({...freshState(),current:s},byId);
  assert.deepEqual(restored.current,s);
});
test('les anciens examens à quatre chapitres et la progression sont conservés',()=>{
  const selected=[1,2,3,4].flatMap(ch=>[
    ...bank.filter(q=>q.chapter===ch&&q.type!=='code').slice(0,5),
    bank.find(q=>q.chapter===ch&&q.type==='code')
  ]);
  const legacy=makeSession(selected,{mode:'exam',title:'Examen blanc',duration:45});
  const q=selected[0];legacy.answers[q.id]=[...q.answer];legacy.marked=[q.id];legacy.index=3;
  const history=JSON.parse(JSON.stringify(legacy));history.id='examen-ancien-remis';history.status='submitted';history.submittedAt=Date.now();
  const state=freshState();state.current=legacy;state.history=[history];
  state.progress[q.id]={attempts:2,correct:1,wrong:1,streak:1,lastAt:1234};state.favorites=[q.id];
  const restored=validateState(JSON.parse(JSON.stringify(state)),byId);
  assert.deepEqual(restored.progress,state.progress);assert.deepEqual(restored.favorites,state.favorites);
  assert.deepEqual(restored.current.answers,legacy.answers);assert.equal(restored.current.index,3);
  assert.deepEqual(restored.current.examChapters,[1,2,3,4]);assert.match(restored.current.title,/Ancien examen/);
  assert.equal(restored.history[0].id,history.id);assert.deepEqual(restored.history[0].examChapters,[1,2,3,4]);
  legacy.examChapters=[2,3];assert.throws(()=>validateState({...state,current:legacy},byId),/Composition/);
});
test('un examen déséquilibré ou une banque 2–3 insuffisante est refusé',()=>{
  assert.throws(()=>generateExam(bank.filter(q=>q.chapter!==3&&q.chapter!==2)),/insuffisante/);
  assert.throws(()=>generateExam(bank.filter(q=>q.id!=='c2-e001'&&(q.chapter!==2||q.type!=='code'||q.id==='c2-e002'))),/insuffisante/);
  const s=generateExam(bank);const i=s.items.findIndex(i=>byId.get(i.id).chapter===2&&byId.get(i.id).type!=='code');
  const extra=bank.find(q=>q.chapter===3&&q.type!=='code'&&!s.items.some(i=>i.id===q.id));
  s.items[i]={id:extra.id,order:extra.options.map(o=>o.id)};
  assert.equal(hasExamComposition(s.items,byId,[2,3]),false);
  assert.throws(()=>validateState({...freshState(),current:s},byId),/Composition/);
});
test('les énoncés et contextes ne renvoient plus à un exemple ou document absent',()=>{
  const missingReference=/\b(?:du cours|le cours|dans l.exemple|dans le schéma|dans le support|la capture|diapositive \d|stratégie [12]|signatures du cours|getters du cours)\b/i;
  for(const q of bank)assert.doesNotMatch(`${q.prompt} ${q.context||''}`,missingReference,q.id);
  for(const id of ['c1-q020','c1-q023','c1-q035','c2-q006','c2-q017','c2-q022','c2-q025','c2-q029','c2-q037','c3-q025','c3-q027','c4-q012','c4-q027','c4-q028','c4-q046'])
    assert.ok(byId.get(id).code?.trim(),`${id} doit afficher son extrait`);
  for(const id of ['c2-e004','c2-e010','c3-e002','c3-e006','c3-e008','c3-e011','c4-e004','c4-e010'])
    assert.ok(byId.get(id).context.length>70,`${id} doit fournir le contrat utile`);
});
test('les nouveaux exemples autonomes donnent les résultats attendus en PHP',()=>{
  for(const [id,after,expected] of [
    ['c2-q017','echo $p->societe;','inconnu'],
    ['c2-q022','echo (new ReflectionProperty(Voiture::class,"disponible"))->getValue($v) ? "true" : "false";','true'],
    ['c2-q029','','CréationFin du programmeDestruction'],
    ['c2-q037','','12']
  ]) {
    const r=spawnSync('php',[],{input:'<?php\n'+byId.get(id).code+'\n'+after,encoding:'utf8'});
    assert.equal(r.status,0,`${id}: ${r.stderr}`);assert.equal(r.stdout,expected,id);
  }
});
test('tous les extraits PHP ajoutés aux QCM passent la vérification de syntaxe',()=>{
  for(const q of bank.filter(q=>q.type!=='code'&&q.code&&!q.code.trimStart().startsWith('<form'))){
    let code=q.code;
    if(/^(public|private|protected)\b/m.test(code)&&!/^class\s/m.test(code))code=`class Exemple {${code}}`;
    const r=spawnSync('php',['-l'],{input:'<?php\n'+code,encoding:'utf8'});
    assert.equal(r.status,0,`${q.id}: ${r.stdout} ${r.stderr}`);
  }
});
