import {shuffle, makeSession} from './quiz.js';

export const EXAM_CHAPTERS = Object.freeze([2, 3]);
export const EXAM_COUNTS = Object.freeze({qcm: 10, code: 2});

// Les anciens examens restent lisibles sans élargir le périmètre des nouveaux.
export function hasExamComposition(items, byId, chapterIds = EXAM_CHAPTERS) {
  if (!Array.isArray(chapterIds) || ![[2, 3], [1, 2, 3, 4]].some(scope =>
    scope.length === chapterIds.length && scope.every((id, i) => id === chapterIds[i]))) return false;
  if (items.length !== 24 || new Set(items.map(item => item.id)).size !== 24) return false;
  const questions = items.map(item => byId.get(item.id));
  if (questions.some(q => !q || !chapterIds.includes(q.chapter))) return false;
  return chapterIds.every(chapter =>
    questions.filter(q => q.chapter === chapter && q.type !== 'code').length === 20 / chapterIds.length &&
    questions.filter(q => q.chapter === chapter && q.type === 'code').length === 4 / chapterIds.length);
}

export function generateExam(bank, config = {}) {
  const selected = [];
  for (const chapter of EXAM_CHAPTERS) {
    const qcm = shuffle(bank.filter(q => q.chapter === chapter && q.type !== 'code'));
    const code = shuffle(bank.filter(q => q.chapter === chapter && q.type === 'code'));
    if (qcm.length < EXAM_COUNTS.qcm || code.length < EXAM_COUNTS.code)
      throw new Error(`Banque insuffisante au chapitre ${chapter}.`);
    selected.push(...qcm.slice(0, EXAM_COUNTS.qcm), ...code.slice(0, EXAM_COUNTS.code));
  }
  if (config.previousIds?.length === 24 && selected.every(q => config.previousIds.includes(q.id))) {
    const chapter = EXAM_CHAPTERS[0];
    const alternative = bank.find(q => q.chapter === chapter && q.type !== 'code' && !config.previousIds.includes(q.id));
    if (alternative) selected[selected.findIndex(q => q.chapter === chapter && q.type !== 'code')] = alternative;
  }
  const session = makeSession(selected, {...config, mode: 'exam', title: 'Examen blanc · chapitres 2 et 3', immediate: false});
  session.examChapters = [...EXAM_CHAPTERS];
  return session;
}
