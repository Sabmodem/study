const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', function (line) {
    line.split(' ').map(Number).sort((a,b) => a - b).reduce((prev, cur) => {
      (cur - prev > 1) ? console.log(cur-1) : '';
      return cur;
    });
});
