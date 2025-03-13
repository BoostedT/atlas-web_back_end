export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';
/* eslint-disable arrow-parens */
  return Array.from(set)
    .filter(value => typeof value === 'string' && value.startsWith(startString))
    .map(value => value.slice(startString.length))
    .join('-');
}
