from re import search

# Selenium and automating a real web browser on the web is a bit finicky
# So a lot of the try catch statements are protecting errors

def getSiteStories(browser, url):
        try:
            browser.get(url)
        except Exception as e:
            return []

        return browser.find_elements_by_xpath("//a[@href]")

def extractLinks(tags, regex):
    href = []

    for a in tags:
        try:
            href.append(a.get_attribute('href'))
        except Exception as e:
            continue

    return [link for link in href if search(regex, link)]

def getStory(body, xpath):
        story = body.find_elements_by_css_selector(xpath)
        return "\n".join([x.text for x in story if len(x.text) > 0])

def getOgDetails(header):
        date = header.find_element_by_xpath('//meta[contains(@name, "pubdate")]')
        title = header.find_element_by_xpath('//meta[contains(@property, "og:title")]')
        desc = header.find_element_by_xpath('//meta[contains(@name, "description")]')

        return {
                'date': date.get_attribute('content') if date else '2017-01-01',
                'title': title.get_attribute('content') if title else 'Unknown',
                'description': desc.get_attribute('content') if desc else 'description'
        }

def scrapeSite(browser, siteDetails):
        aTags = getSiteStories(browser, siteDetails['url'])
        links = extractLinks(aTags, siteDetails['link_regex'])
        stories = []

        for link in links:
            try:
                browser.get(link)
                browser.implicitly_wait(2)
                details = getOgDetails(browser.find_element_by_css_selector('head'))
                story = getStory(browser.find_element_by_css_selector('body'), siteDetails['story_xpath'])

                stories.append({
                    'url': link,
                    'date': details['date'],
                    'title': details['title'],
                    'desc': details['description'],
                    'story': story
                })

            except Exception as e:
                continue

        return stories
