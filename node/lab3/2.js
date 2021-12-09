const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const check_parity = (num) => num % 2 != 0;

rl.on('line', function (line) {
  console.log(...line.split(' ').filter((obj) => check_parity(Number(obj))));
});
