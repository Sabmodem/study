const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', function (line) {
  console.log(line.split(' ').map(Number).sort((a,b) => a - b).splice(0,3).reduce((num1, num2) => num1 + num2));
});
