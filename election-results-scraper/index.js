const fs = require('fs');
const getElectionDates = require('./getElectionDates');
const getElectionResults = require('./getElectionResults');
const dates = require('../data/source/election_dates.json');

(async () => {
  const loadedDates = fs.readdirSync('./downloads').map((f) => f.split('_')[0]);
  const datesToLoad = dates.filter((d) => !loadedDates.includes(d.date));
  console.log(`Loading ${datesToLoad.length} dates...`);
  await getElectionResults(datesToLoad);
})();
