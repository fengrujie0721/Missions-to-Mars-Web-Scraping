# Web-Scraping-Challenge

Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML.

Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables.

![image](https://user-images.githubusercontent.com/79819331/120661928-b4886000-c456-11eb-9906-9d1335487075.png)



Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com). Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.


![image](https://user-images.githubusercontent.com/79819331/120662439-252f7c80-c457-11eb-9e87-e386925f7ec0.png)


Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.


![image](https://user-images.githubusercontent.com/79819331/120662791-6c1d7200-c457-11eb-8a4a-121c7a27e854.png)


![image](https://user-images.githubusercontent.com/79819331/120663048-aedf4a00-c457-11eb-8ad4-7e2208ab0460.png)


![image](https://user-images.githubusercontent.com/79819331/120663325-eb12aa80-c457-11eb-8a7b-f0def8c44b2f.png)


![image](https://user-images.githubusercontent.com/79819331/120663717-447ad980-c458-11eb-9daf-28ffcb28142d.png)



Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres. Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

![image](https://user-images.githubusercontent.com/79819331/120664042-97ed2780-c458-11eb-8d6a-d103943855f9.png)


![image](https://user-images.githubusercontent.com/79819331/120664215-bf43f480-c458-11eb-931b-896a0da90195.png)


Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

![image](https://user-images.githubusercontent.com/79819331/120664773-35e0f200-c459-11eb-85e9-6075df9de416.png)


![image](https://user-images.githubusercontent.com/79819331/120665249-9a03b600-c459-11eb-97c3-d050405de7eb.png)







