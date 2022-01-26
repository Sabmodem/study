const _ = require('lodash');

console.log(
  _(require('./clients.json').clients)
    .filter((obj) => obj.address.city == 'Кунгур')
    .orderBy(['gender','age','name'], ['asc','desc','asc'])
    .value());
