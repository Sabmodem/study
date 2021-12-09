const fs = require('fs');
const _ = require('lodash');

console.log(
  _(require('./colors.json'))
    .filter((obj) => _.keys(obj)[0].length < 6)
    .sortBy((obj) => _.keys(obj)[0])
    .map((obj) => _.keys(obj)[0])
    .value()
)
