from redis import Redis
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

from scraper.scraper import scrapeSite
from scraper.nlp import processTxt
from scraper.sites import sites

# Config
redis = Redis(host='redis', port=6379)
browser = webdriver.Remote(
    command_executor='http://browser:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)


# Quick Utility functions
def appendNlp(result):
    combinedTxt = "\n".join([result['title'], result['desc'], result['story']])

    return { **result, **processTxt(combinedTxt) }

def setStory(url, info):
    info = json.dumps(info)
    redis.pipeline().set('url:' + url, info).expire(url, 3600000).execute()

    return

def isStorySet(url):
    return redis.exists('url:' + url)

# Application
browser.implicitly_wait(2)

work = [sites['cnn'], sites['wallStreetJournal']]

while True:
    for job in work:
        for x in [appendNlp(x) for x in scrapeSite(browser, job) if not isStorySet(x['url'])]:
            setStory(x['url'], x)
