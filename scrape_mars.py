import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import requests

scraped_data:{}

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_mars():
    browser = init_browser()
    
    # site number 1
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    for n in range(1):
        html=browser.html
        soup=bs(html,'html.parser')
        news_title = soup.find('div',class_="content_title").text
        # print(news_title)
    for n in range(1):
        html=browser.html
        soup=bs(html,'html.parser')
        body_text=soup.find('div',class_="article_teaser_body").text
    
    # site number 2
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    s_url = 'https://www.jpl.nasa.gov'
    browser.visit(url)

    html=browser.html
    soup=bs(html,'html.parser')

    featured_image = soup.find('article',class_="carousel_item")['style']
    featured_image = featured_image[23:-3]
    featured_image_path = s_url + featured_image
    
    # site number 3
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html=browser.html
    soup=bs(html,'html.parser')

    tweet = soup.find('p',class_='tweet-text')
    tweet = tweet.find(text=True, recursive=False)

    # site number 4
    facts_url = 'https://space-facts.com/mars/'
    facts_df = pd.read_html(facts_url)[0]
    table_content = facts_df.to_html()

    # site number 5
    # first hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    s_url = 'https://astrogeology.usgs.gov'
    browser.visit(url)
    xpath = '//*[@id="product-section"]/div[2]/div[1]/div/a'
    browser.find_by_xpath(xpath).click()

    html=browser.html
    soup=bs(html,'html.parser')
    cerberus = soup.find('div',class_="container").find_all('img')[2]['src']
    cerberus_path = s_url + cerberus

    # second hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    s_url = 'https://astrogeology.usgs.gov'
    browser.visit(url)
    xpath = '//*[@id="product-section"]/div[2]/div[2]/div/a'
    browser.find_by_xpath(xpath).click()

    html=browser.html
    soup=bs(html,'html.parser')
    schiaparelli = soup.find('div',class_="container").find_all('img')[2]['src']
    schiaparelli_path = s_url + schiaparelli

    # third hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    s_url = 'https://astrogeology.usgs.gov'
    browser.visit(url)
    xpath = '//*[@id="product-section"]/div[2]/div[3]/div/a'
    browser.find_by_xpath(xpath).click()

    html=browser.html
    soup=bs(html,'html.parser')
    syrtis = soup.find('div',class_="container").find_all('img')[2]['src']
    syrtis_path = s_url + syrtis

    # fourth hemisphere
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    s_url = 'https://astrogeology.usgs.gov'
    browser.visit(url)
    xpath = '//*[@id="product-section"]/div[2]/div[4]/div/a'
    browser.find_by_xpath(xpath).click()

    html=browser.html
    soup=bs(html,'html.parser')

    valles = soup.find('div',class_="container").find_all('img')[2]['src']
    valles_path = s_url + valles

    # this dictionary will hold everything we pull from all the sites
    scraped_data = {'title':news_title,
                    'body':body_text,
                    'feature_image':featured_image_path,
                    'table': table_content,
                    'weather':tweet,
                    'cerebus':cerberus_path,
                    'schiaparelli':schiaparelli_path,
                    'syrtis':syrtis_path,
                    'valles':valles_path
                    }
    # print(scraped_data)

    browser.quit()

    return scraped_data

