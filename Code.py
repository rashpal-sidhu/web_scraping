# This is the code for the basic web scraping of IMBD website for top rated movies of all time
# Disclaimer: You should first look at the website policy before scraping it to make sure it is legal to scrape it.

#Code: 

#Import required libraries
import requests
import bs4

#Making a http request to get the webpage information and all the material of the webpage
response = requests.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")

#Checking the status code to ensure that the request to the webpage was successful(successful = 200; unsuccessful = 400)
response.status_code
response.text
soup_obj = bs4.BeautifulSoup(response.text,'lxml')
soup_obj.prettify()

#Get the title of the web page and compare it with the actual page that you want to scrape to make sure you are proceeding in the right direction
soup_obj.select('title')[0].getText()
trs =  soup_obj.find_all('tr')
movies_list = []
for tr in trs:
    if tr.find('td',{'class', 'titleColumn'}) == None:
        continue
    movies_list.append((tr.find('td',{'class', 'titleColumn'}).find('a').getText()))
for movies in movies_list:
    print(movies)


