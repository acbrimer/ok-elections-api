const puppeteer = require('puppeteer');
const fs = require('fs');

const rootUrl =
  'https://oklahoma.gov/elections/elections-results/election-results/';
let electionDates = [];

async function getElectionDates() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  for (let year = 2008; year <= 2022; year++) {
    const url = `${rootUrl}${year}-election-results.html`;
    await page.goto(url);
    const data = await page.evaluate(() =>
      Array.from(document.querySelectorAll('table > tbody > tr'), (row) =>
        Array.from(row.querySelectorAll('td'), (cell) => cell.innerText)
      )
    );
    const d = data
      .filter((f) => f.length > 0)
      .map((r) => ({
        date: new Date(Date.parse(`${r[0]}, ${year}`))
          .toISOString()
          .slice(0, 10)
          .replaceAll('-', ''),
        label: r[1],
      }));

    electionDates = [...electionDates, ...d];
  }

  fs.writeFile(
    '../data/source/election_dates.json',
    JSON.stringify(electionDates),
    (err) => {
      if (err) {
        console.error(err);
        return;
      }
      //file written successfully
    }
  );
  browser.close();
  return electionDates;
}

module.exports = getElectionDates;
