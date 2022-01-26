const _ = require('lodash');

console.log(
  _(require('./users.json'))
    .filter((obj) => obj.address.geo.lat < 0)
    .map((obj) => {
      return {
        username: obj.username,
        city: obj.address.city
      };
    }).orderBy('city', 'desc')
    .value());
