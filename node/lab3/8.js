const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', function (line) {
  line.split(' ').reduce((prev, cur, i, arr) => {
    arr.filter((obj) => {
      return cur == obj;
    }).length == 1 ? console.log(cur): '';
    return cur;
  });
});
