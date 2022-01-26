const _ = require('lodash');

console.log(_(require('./colors.json'))
  .map((obj) => {
    const color = _.keys(obj)[0];
    return {
      color,
      rgb: [obj[color][0], obj[color][1], obj[color][2]]
    };
  }).sortBy('color').value());
