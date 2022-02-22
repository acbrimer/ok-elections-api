# Election Results Scraper

A super simple node/puppeteer webscraper to download CSV election results from OK election board portal.

The OK Election Results portal appears to be built on a C#/Angular stack (based on IIS hosting and all of the `_ng...` tags). The 'Export' buttons trigger calls to a download link I was able to see intercepting network calls, but unfortunately COORS is blocking me from hitting these paths.

I figured that building a simple web scraper to hit each election date (using the `elecDate` URL param) and clicking the download buttons for all 3 CSV files would be probably less time consuming and definitely more fun than clicking through each of the pages. While I was initially looking at a python solution (BeautifulSoup) for web scraping integrate with the rest of the ETL code, I found node puppeteer to be far more straightforward and was able to produce a working solution in under an hour.
