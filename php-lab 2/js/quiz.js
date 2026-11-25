export function shuffle(values, rng = Math.random) {
  const out = [...values];
  for (let i = out.length - 1; i > 0; i--) { const j = Math.floor(rng() * (i + 1)); [out[i], out[j]] = [out[j], out[i]]; }
  return out;
}
export const isAnswered = (q, value) => q.type === 'code' ? typeof value === 'string' && value.trim().length > 0 : Array.isArray(value) && value.length > 0;
export const exactAnswer = (q, value) => Array.isArray(value) && value.length === q.answer.length && new Set(value).size === value.length && q.answer.every(x => value.includes(x));
export function selectQuestions(bank, config) {
  return bank.filter(q => config.chapters.includes(q.chapter) && (config.difficulty === 'all' || q.difficulty === config.difficulty) && (config.type === 'all' || q.type === config.type) && (!config.onlyCode || q.type === 'code') && (!config.onlyQcm || q.type !== 'code'));
}
export function makeSession(questions, config = {}) {
  if (!questions.length) throw new Error('Aucune question ne correspond à ces critères.');
  const now = Date.now();
  return {id: globalThis.crypto?.randomUUID?.() || `${now}-${Math.random().toString(36).slice(2)}`, mode: config.mode || 'custom', title: config.title || 'Session personnalisée', items: shuffle(questions).map(q => ({id:q.id, order:q.options ? shuffle(q.options.map(o=>o.id)) : []})), answers:{}, marked:[], revealed:[], hints:[], grades:{}, recorded:{}, index:0, startedAt:now, duration:Math.max(0,Number(config.duration)||0)*60, immediate:!!config.immediate, weights:{qcm:Number(config.weights?.qcm)||1, code:Number(config.weights?.code)||5}, status:'active', submittedAt:null};
}
export function sessionScore(session, byId) {
  let earned=0, maximum=0, pending=0, qcmCorrect=0, qcmTotal=0, codeTotal=0;
  for (const item of session.items) {
    const q=byId.get(item.id); if(!q) continue;
    const weight=q.type==='code'?session.weights.code:session.weights.qcm; maximum+=weight;
    if(q.type==='code') { codeTotal++; if(session.grades[q.id] === undefined) pending++; else earned+=weight*session.grades[q.id]; }
    else { qcmTotal++; if(exactAnswer(q,session.answers[q.id])) {earned+=weight; qcmCorrect++;} }
  }
  return {earned,maximum,pending,qcmCorrect,qcmTotal,codeTotal,percent:maximum?earned/maximum*100:0,score:maximum?earned/maximum*20:0};
}
export function elapsedSeconds(s, now=Date.now()) { return Math.max(0,Math.floor(((s.submittedAt||now)-s.startedAt)/1000)); }
export const remainingSeconds = (s, now=Date.now()) => Math.max(0,s.duration-elapsedSeconds(s,now));
