from splinter import Browser
#from splinter.exceptions import ElementDoesExist
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape():
    # set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    
    #visit redplanetscience.com
    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)
    #scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #get news
    quotes = soup.find_all('div', id='news')

    for quote in quotes:
        #get news title
        news_title=quote.find("div",class_="content_title").get_text()
        #get news paragraph
        news_p=quote.find("div",class_="article_teaser_body").get_text()


    #visit spaceimages-mars.com
    url2="https://spaceimages-mars.com/"
    browser.visit(url2)
    time.sleep(1)
    #scrape page into soup
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    #get floating_text_area
    quotes2 = soup2.find_all('div', class_='floating_text_area')

    for quote in quotes2:
        #get a tag
        link=quote.find('a')
        #get link
        image_url=link["href"]
        #get whole url
        image_src1=url2+image_url

    #visit marshemisphere.com
    url3="https://marshemispheres.com/"
    browser.visit(url3)
    time.sleep(1)
    #scrape page into soup
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')
    #get item
    quotes3 = soup3.find_all('div', class_='item')
    #set up empty list and dictionary
    hemisphere_image_urls=[]
    dic={}
    for quote in quotes3:
        #get img tag     
        title=quote.find("img")
        #get img alt
        title1=title["alt"]
        #split img alt and remove the last two
        title2=title1.split(" ")[0:-2]
        #rejoin the splitted img alt
        title3=" ".join(title2)
        #get img src
        image_url=title["src"]
        #get whole url
        image_url1=url3+image_url
        #set up dictionary
        dic={"title":title3,"img_url":image_url1}
        #append the dictionary to list of hemisphere_image_urls
        hemisphere_image_urls.append(dic)
    #store data in a dictionary
    mars={"news_title":news_title,"news_p":news_p,"featured_image_url":image_src1,"hemisphere_image_urls":hemisphere_image_urls}
    #quit the browser
    browser.quit()
    
    return(mars)
   
    
