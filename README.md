# Dog Digger News
Dogs have taken over the news.

The dictionary folder serves as the different words to replace current ones with. Feel free open a pull request
with more!

## Scraping
The most impart part of the application is to gather data. Most websites are heavily reliant on Javascript,
meaning the days of simply piping responses to GET requests into BeautifulSoup are over.

To counter this, an automated instance of [PhantomJS](http://phantomjs.org/)(A headless browser) via
[Selenium](http://www.seleniumhq.org/) traverses the top news sites at random intervals. The big gains are
that an actual browser is now executing each site's Javascript, while still appearing like an actual visitor.

The speed tradeoff is huge, however it isn't very resource intensive and keeps a steady flow of new pages coming in.

The urls retrieved from the home pages are then filtered for legitimate links that haven't been crawled recently.

Each new url will be scraped and fed into the application's natural language processor.

## Natural Language Processing
Currently the app is using [TextBlob](https://textblob.readthedocs.io/en/dev/) and [NLTK](http://www.nltk.org/).
Not an expert on natural language processing so the stuff is fairly rudimentary. It's mostly just for obtaining
a list of the trending names and nouns in each article.

## Storage
All new stories after being scraped and tagged are inserted into Redis.  Redis is set to only store x number of
stories, where the oldest ones are killed off to make room for new ones.

The decision behind this is two pronged, first it prevents large amounts of space from being take up. Second it
ensures that stories are frequently being shuffled in and out.

## Serving content
Everything is served through [Golang]()'s [Gin Framework]().

## Client Web App
Not much to say about this.

## Todo
- Get containers properly synced
- Figure out the random image situation
- Implement the actual word replacement

