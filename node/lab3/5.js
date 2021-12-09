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
  console.log(
    Math.min(
      ...input.splice(1,input.length)
        .map((i) => i.split(''))
        .filter((num) => num[num.length-1] == '3')
        .map((num) => Number(num.join('')))
    )
  );
});
