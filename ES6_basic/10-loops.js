/* eslint-disable no-param-reassign, no-plusplus */
export default function appendToEachArrayValue(array, appendString) {
  let index = 0;
  for (const value of array) {
    array[index] = appendString + value;
    index++;
  }
  return array;
}
