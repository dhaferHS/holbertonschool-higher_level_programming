#!/usr/bin/node
function nextBiggest (arr) {
  let max = Infinity; let result = -Infinity;

  for (const value of arr) {
    const nr = Number(value);

    if (nr > max) {
      [result, max] = [max, nr];
    } else if (nr < max && nr > result) {
      result = nr;
    }
  }

  return result;
}
const arr = process.argv;
console.log(nextBiggest(arr));
