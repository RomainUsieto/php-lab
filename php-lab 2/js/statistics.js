import {sessionScore} from './quiz.js';
import {needsReview} from './storage.js?v=erreurs-20261125';
export function stats(bank,state) {
  const byId=new Map(bank.map(q=>[q.id,q])), entries=bank.map(q=>state.progress[q.id]).filter(Boolean);
  const attempts=entries.reduce((n,p)=>n+p.attempts,0),correct=entries.reduce((n,p)=>n+p.correct,0);
  const done=entries.length, mastered=entries.filter(p=>p.streak>=3).length,coverage=bank.length?done/bank.length:0,success=attempts?correct/attempts:0;
  const exams=state.history.filter(s=>s.mode==='exam'),finalExams=exams.filter(s=>!sessionScore(s,byId).pending),scores=finalExams.map(s=>sessionScore(s,byId).score);
  return {total:bank.length,done,mastered,attempts,success:success*100,coverage:coverage*100,readiness:Math.round(100*coverage*(.5+.5*success)),remaining:bank.length-mastered,errors:bank.filter(q=>needsReview(state.progress[q.id])),examCount:exams.length,finalExamCount:scores.length,average:scores.length?scores.reduce((a,b)=>a+b,0)/scores.length:null,best:scores.length?Math.max(...scores):null};
}
