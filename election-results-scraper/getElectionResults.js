const puppeteer = require('puppeteer');

async function getCountyResult(date) {
  const url = `https://results.okelections.us/OKER/?elecDate=${date}`;
  return puppeteer
    .launch({ headless: true })
    .then(function (browser) {
      return browser.newPage();
    })
    .then(function (page) {
      return page.goto(url).then(function () {
        page
          .waitForSelector('#dropdownMenu3')
          .then(() => {
            page.click('button#dropdownMenu3').then(() => {
              page
                .waitForSelector(
                  '[aria-label="Export Types"] > button:nth-child(6)'
                )
                .then(() => {
                  page._client
                    .send('Page.setDownloadBehavior', {
                      behavior: 'allow',
                      downloadPath: './scraped_files',
                    })
                    .then(() => {
                      page
                        .click(
                          '[aria-label="Export Types"] > button:nth-child(6)'
                        )
                        .then(() => true);
                    });
                });
            });
          })
          .catch((err) => {
            console.log('Err', err);
            return false;
          });
      });
    })
    .catch(function (err) {
      console.log(`ERROR: could not get results for ${date}`, err);
      return false;
    });
}

async function getPrecinctResult(date) {
  const url = `https://results.okelections.us/OKER/?elecDate=${date}`;
  return puppeteer
    .launch({ headless: true })
    .then(function (browser) {
      return browser.newPage();
    })
    .then(function (page) {
      return page.goto(url).then(function () {
        page
          .waitForSelector('#dropdownMenu3')
          .then(() => {
            page.click('button#dropdownMenu3').then(() => {
              page
                .waitForSelector(
                  '[aria-label="Export Types"] > button:nth-child(9)'
                )
                .then(() => {
                  page._client
                    .send('Page.setDownloadBehavior', {
                      behavior: 'allow',
                      downloadPath: './scraped_files',
                    })
                    .then(() => {
                      page
                        .click(
                          '[aria-label="Export Types"] > button:nth-child(9)'
                        )
                        .then(() => true);
                    });
                });
            });
          })
          .catch((err) => {
            console.log('Err', err);
            return false;
          });
      });
    })
    .catch(function (err) {
      console.log(`ERROR: could not get results for ${date}`, err);
      return false;
    });
}

async function getStateResult(date) {
  const url = `https://results.okelections.us/OKER/?elecDate=${date}`;
  return puppeteer
    .launch({ headless: true })
    .then(function (browser) {
      return browser.newPage();
    })
    .then(function (page) {
      return page.goto(url).then(function () {
        page
          .waitForSelector('#dropdownMenu3')
          .then(() => {
            page.click('button#dropdownMenu3').then(() => {
              page
                .waitForSelector(
                  '[aria-label="Export Types"] > button:nth-child(3)'
                )
                .then(() => {
                  page._client
                    .send('Page.setDownloadBehavior', {
                      behavior: 'allow',
                      downloadPath: './scraped_files',
                    })
                    .then(() => {
                      page
                        .click(
                          '[aria-label="Export Types"] > button:nth-child(3)'
                        )
                        .then(() => true);
                    });
                });
            });
          })
          .catch((err) => {
            console.log('Err', err);
            return false;
          });
      });
    })
    .catch(function (err) {
      console.log(`ERROR: could not get results for ${date}`, err);
      return false;
    });
}

async function getElectionResults(dates) {
  for (let i = 0; i < dates.length; i++) {
    console.log(dates[i]);
    await Promise.all([
      await getPrecinctResult(dates[i].date),
      await getCountyResult(dates[i].date),
      await getStateResult(dates[i].date),
    ]).then((r) => console.log(r ? ' success' : ' fail'));
  }
}

module.exports = getElectionResults;
