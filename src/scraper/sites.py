# This is the configuration for all sites to be scraped.
#
# The scraper will only get the front page, we are only looking for trending news.
#
# The link_regex will be the regex to match all links on the home page for.
#
# The story_xpath is a bit more driver specific, but it's  a css selector to get the story text.

sites = {
    'cnn': {
        'url': 'https://www.cnn.com',
        'link_regex': 'https?:\/\/(www.)?cnn.com\/20*',
        'story_xpath': '.zn-body__paragraph'
    },
    'bbc': {
        'url': 'http://www.bbc.com/',
        'link_regex': 'https?:\/\/www.bbc.com\/news\/*',
        'story_xpath': '.articleBody'
    },
    'nyTimes': {
        'url': 'https://www.nytimes.com/',
        'link_regex': 'https?:\/\/www.nytimes.com\/20*',
        'story_xpath': '.story-body-text'
    },
    'guardian': {
        'url': 'https://www.theguardian.com',
        'link_regex': 'https?:\/\/www.theguardian.com\/us-news\/*',
        'story_xpath': '.content__article-body'
    },
    'usaToday': {
        'url': 'https://www.usatoday.com',
        'link_regex': 'https?:\/\/www.usatoday.com\/story\/*',
        'story_xpath': '.p-text'
    },
    'eOnline': {
        'url': 'http://wwww.eonline.com',
        'link_regex': 'https?:\/\/www.eonline.com\/news\/*',
        'story_xpath': '.post-content'
    },
    'wallStreetJournal': {
        'url': 'https://www.wsj.com',
        'link_regex': 'https?:\/\/www.wsj.com\/articles\/*',
        'story_xpath': '.wsj-snippet-body'
    }
}
