const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];

rl.on('line', function (line) {
  input.push(line);
});

rl.on('close', function () {
  console.log(input.sort((a,b) => Number(b.split(';')[1] - Number(a.split(';')[1])))[input[0]].split(';')[0]);
});
