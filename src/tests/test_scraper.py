from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from scraper import scraper
from scraper.sites import sites

browser = webdriver.Remote(
    command_executor='http://browser:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)

browser.implicitly_wait(2)

# Tests that we can get a tags off the home page
def test_cnn_scrape():
    siteStories = scraper.getSiteStories(browser, sites['cnn']['url'])
    assert len(siteStories) > 0

# Tests that our regex works
def test_cnn_regex():
    siteStories = scraper.getSiteStories(browser, sites['cnn']['url'])
    siteStories = scraper.extractLinks(siteStories, sites['cnn']['link_regex'])
    assert len(siteStories) > 0

# Tests that we can get a tags off the home page
def test_bbc_scrape():
    siteStories = scraper.getSiteStories(browser, sites['bbc']['url'])
    assert len(siteStories) > 0

# Tests that our regex works
def test_bbc_regex():
    siteStories = scraper.getSiteStories(browser, sites['bbc']['url'])
    siteStories = scraper.extractLinks(siteStories, sites['bbc']['link_regex'])
    assert len(siteStories) > 0

# Tests that we can get a tags off the home page
def test_nyTimes_scrape():
    siteStories = scraper.getSiteStories(browser, sites['nyTimes']['url'])
    assert len(siteStories) > 0

# Tests that our regex works
def test_nyTimes_regex():
    siteStories = scraper.getSiteStories(browser, sites['nyTimes']['url'])
    siteStories = scraper.extractLinks(siteStories, sites['nyTimes']['link_regex'])
    assert len(siteStories) > 0

# Tests that we can get a tags off the home page
def test_guardian_scrape():
    siteStories = scraper.getSiteStories(browser, sites['guardian']['url'])
    assert len(siteStories) > 0

# Tests that our regex works
def test_guardian_regex():
    siteStories = scraper.getSiteStories(browser, sites['guardian']['url'])
    siteStories = scraper.extractLinks(siteStories, sites['guardian']['link_regex'])
    assert len(siteStories) > 0
