export const KEY='php-lab-v1';
export function freshState() { return {version:1,progress:{},favorites:[],history:[],current:null,prefs:{theme:'light',duration:45,qcmWeight:1,codeWeight:5}}; }
const plain=x=>x!==null&&typeof x==='object'&&!Array.isArray(x);
const finite=x=>typeof x==='number'&&Number.isFinite(x);
export function validateState(data, byId) {
  if(!plain(data)||data.version!==1||!plain(data.progress)||!Array.isArray(data.favorites)||!Array.isArray(data.history)||!plain(data.prefs)) throw new Error('Ce fichier n’est pas une sauvegarde PHP Lab version 1.');
  const state=freshState();
  for(const [id,p] of Object.entries(data.progress)) {
    if(!byId.has(id)) continue;
    if(!plain(p)||!['attempts','correct','streak','wrong'].every(k=>Number.isInteger(p[k])&&p[k]>=0)||p.correct>p.attempts||p.wrong>p.attempts||p.streak>p.correct||p.correct+p.wrong!==p.attempts) throw new Error('Statistiques incohérentes.');
    state.progress[id]={attempts:p.attempts,correct:p.correct,streak:p.streak,wrong:p.wrong,lastAt:finite(p.lastAt)?p.lastAt:0};
  }
  state.favorites=[...new Set(data.favorites.filter(id=>typeof id==='string'&&byId.has(id)))];
  state.prefs={theme:['light','dark'].includes(data.prefs.theme)?data.prefs.theme:'light',duration:Math.min(180,Math.max(1,Number(data.prefs.duration)||45)),qcmWeight:Math.min(20,Math.max(.25,Number(data.prefs.qcmWeight)||1)),codeWeight:Math.min(20,Math.max(.25,Number(data.prefs.codeWeight)||5))};
  function session(raw) {
    if(!plain(raw)||typeof raw.id!=='string'||!Array.isArray(raw.items)||!raw.items.length||raw.items.length>260||!finite(raw.startedAt)||!plain(raw.answers)||!plain(raw.grades)||!['active','submitted'].includes(raw.status)) throw new Error('Session invalide.');
    const ids=raw.items.map(x=>x?.id);if(new Set(ids).size!==ids.length||ids.some(id=>!byId.has(id)))throw new Error('Questions de session inconnues ou répétées.');
    const s={id:raw.id.slice(0,100),mode:['exam','custom','chapter','code','errors','express'].includes(raw.mode)?raw.mode:'custom',title:typeof raw.title==='string'?raw.title.slice(0,100):'Session',items:[],answers:{},grades:{},recorded:{},marked:[],revealed:[],hints:[],index:Math.min(ids.length-1,Math.max(0,Math.floor(Number(raw.index)||0))),startedAt:raw.startedAt,duration:Math.max(0,Math.min(10800,Number(raw.duration)||0)),immediate:!!raw.immediate,weights:{qcm:Math.min(20,Math.max(.25,Number(raw.weights?.qcm)||1)),code:Math.min(20,Math.max(.25,Number(raw.weights?.code)||5))},status:raw.status,submittedAt:finite(raw.submittedAt)?raw.submittedAt:null};
    for(const item of raw.items){const q=byId.get(item.id), allowed=q.options?.map(o=>o.id)||[]; const order=Array.isArray(item.order)?item.order:[];s.items.push({id:q.id,order:order.length===allowed.length&&new Set(order).size===allowed.length&&order.every(x=>allowed.includes(x))?order:allowed});const a=raw.answers[q.id];if(q.type==='code') {if(typeof a==='string')s.answers[q.id]=a.slice(0,30000);if([0,.5,1].includes(raw.grades[q.id]))s.grades[q.id]=raw.grades[q.id];}else if(Array.isArray(a)&&new Set(a).size===a.length&&a.every(x=>allowed.includes(x))&&(q.type==='multiple'||a.length<=1))s.answers[q.id]=a;if(raw.recorded?.[q.id]===true)s.recorded[q.id]=true;}
    for(const key of ['marked','revealed','hints'])s[key]=Array.isArray(raw[key])?[...new Set(raw[key].filter(id=>ids.includes(id)))]:[];
    if(s.mode==='exam'&&(s.items.length!==24||s.immediate||[1,2,3,4].some(c=>s.items.filter(i=>byId.get(i.id).chapter===c&&byId.get(i.id).type!=='code').length!==5||s.items.filter(i=>byId.get(i.id).chapter===c&&byId.get(i.id).type==='code').length!==1)))throw new Error('Composition d’examen invalide.');
    if(s.status==='submitted'&&!s.submittedAt)throw new Error('Date de remise manquante.');
    if(s.status==='active'&&s.mode==='exam'){s.revealed=[];s.grades={};s.recorded={};}
    return s;
  }
  state.history=data.history.slice(-100).map(session).filter(s=>s.status==='submitted');
  if(data.current)state.current=session(data.current);
  return state;
}
export function loadState(byId) { try {const raw=localStorage.getItem(KEY);return raw?validateState(JSON.parse(raw),byId):freshState();}catch {return freshState();} }
export function saveState(state) {try{localStorage.setItem(KEY,JSON.stringify(state));return true;}catch{return false;} }
export function recordAttempt(state,s,q,success) {
  if(s.recorded[q.id])return;
  const p=state.progress[q.id]||{attempts:0,correct:0,wrong:0,streak:0,lastAt:0};
  p.attempts++;if(success){p.correct++;p.streak++;}else{p.wrong++;p.streak=0;}p.lastAt=Date.now();state.progress[q.id]=p;s.recorded[q.id]=true;
}
export function archiveSession(state,s){const ix=state.history.findIndex(h=>h.id===s.id);const copy=JSON.parse(JSON.stringify(s));if(ix>=0)state.history[ix]=copy;else state.history.push(copy);state.history=state.history.slice(-100);}
