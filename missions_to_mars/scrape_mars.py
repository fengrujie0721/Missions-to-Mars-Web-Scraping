from splinter import Browser
#from splinter.exceptions import ElementDoesExist
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    

    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.find_all('div', id='news')

    for quote in quotes:
        news_title=quote.find("div",class_="content_title").get_text()
        news_p=quote.find("div",class_="article_teaser_body").get_text()


    
    url2="https://spaceimages-mars.com/"
    browser.visit(url2)
    time.sleep(1)
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')
    quotes2 = soup2.find_all('div', class_='floating_text_area')

    for quote in quotes2:
        link=quote.find('a')
        image_url=link["href"]
        
        image_src1=url2+image_url

    url3="https://marshemispheres.com/"
    browser.visit(url3)
    time.sleep(1)
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')

    quotes3 = soup3.find_all('div', class_='item')
    hemisphere_image_urls=[]
    dic={}
    for quote in quotes3:
              
        title=quote.find("img")
        title1=title["alt"]
        title2=title1.split(" ")[0:-2]
    
        title3=" ".join(title2)
        image_url=title["src"]
        image_url1=url3+image_url
        dic={"title":title3,"img_url":image_url1}
        hemisphere_image_urls.append(dic)
    
    mars={"news_title":news_title,"news_p":news_p,"featured_image_url":image_src1,"hemisphere_image_urls":hemisphere_image_urls}
    browser.quit()
    
    return(mars)
    # Quit the browser
    
    
