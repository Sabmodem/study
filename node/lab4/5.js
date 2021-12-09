const fs = require('fs');
const _ = require('lodash');

const argb2hex = (channels) => {
  return (`#${channels.map(entry => (`0${entry.toString(16)}`).slice(-2)).join('')}`);
};

console.log(
  _(_.zip(require('./data.js').colors, require('./data.js').argb))
    .map((obj) => _.zipObject(['color','hex_name'],[ obj[0],argb2hex( [obj[1][0],obj[1][1],obj[1][2]] )]))
    .orderBy('color','ask')
    .value());
