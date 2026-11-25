import {shuffle, makeSession} from './quiz.js';
export function generateExam(bank, config={}) {
  const selected=[];
  for(let chapter=1;chapter<=4;chapter++) {
    const qcm=shuffle(bank.filter(q=>q.chapter===chapter&&q.type!=='code'));
    const code=shuffle(bank.filter(q=>q.chapter===chapter&&q.type==='code'));
    if(qcm.length<5 || code.length<1) throw new Error(`Banque insuffisante au chapitre ${chapter}.`);
    selected.push(...qcm.slice(0,5),code[0]);
  }
  // Même si le tirage répète exactement la copie précédente, remplacer un QCM.
  if(config.previousIds?.length===24 && selected.every(q=>config.previousIds.includes(q.id))) {
    const alternative=bank.find(q=>q.chapter===1&&q.type!=='code'&&!config.previousIds.includes(q.id));
    if(alternative)selected[selected.findIndex(q=>q.chapter===1&&q.type!=='code')]=alternative;
  }
  return makeSession(selected,{...config,mode:'exam',title:'Examen blanc',immediate:false});
}
