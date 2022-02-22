const puppeteer = require('puppeteer');

function downloadElectionDateFiles(url) {
  puppeteer
    .launch({ headless: false })
    .then(function (browser) {
      return browser.newPage();
    })
    .then(function (page) {
      return page.goto(url).then(function () {
        page.waitForSelector('#dropdownMenu3').then(() => {
          page.click('button#dropdownMenu3').then(() => {
            page
              .waitForSelector(
                '[aria-label="Export Types"] > button:nth-child(6)'
              )
              .then(() => {
                page._client
                  .send('Page.setDownloadBehavior', {
                    behavior: 'allow',
                    downloadPath: './downloads',
                  })
                  .then(() => {
                    page.click(
                      '[aria-label="Export Types"] > button:nth-child(6)'
                    );
                  });
              });
          });
        });

        page.waitForSelector('#dropdownMenu3').then(() => {
          page.click('button#dropdownMenu3').then(() => {
            page
              .waitForSelector(
                '[aria-label="Export Types"] > button:nth-child(9)'
              )
              .then(() => {
                page.click('[aria-label="Export Types"] > button:nth-child(9)');
              });
          });
        });
      });
    })
    .catch(function (err) {
      console.log('Error opening URL', err);
    });
}

downloadElectionDateFiles(
  'https://results.okelections.us/OKER/?elecDate=20211109'
);
