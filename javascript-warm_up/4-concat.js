#!/usr/bin/node
const argv = process.argv;
if (process.argv[2] === undefined) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
