
from bs4 import BeautifulSoup
import pandas as pd

with open("../documents/Humphrey's 3-course menu - Humphrey's Restaurants.html") as f:
    page = BeautifulSoup(f, "lxml")

 # url of the webiste you can save it and chnage the path https://humphreys.nl/en/3-course-menu/    

#selecting the pages
title = page.select("title")
header_text = page.select("h1")
header_details = page.select("h2")
destcription = page.select(".fusion-text")

#assigning varibles
page_tittle = title[0].get_text()
page_header = header_text[0].get_text()
page_header_details = header_details[0].get_text()
details = destcription[1].get_text()
menu_info = destcription[2].get_text()
menu_decrtiption = destcription[3].get_text()
menu_children = destcription[4].get_text()
detail_menu = f"Children menus:  {menu_children}"


print("tittle : " + page_tittle)
print("header : " + page_header)
print("header info :" + page_header_details)
print("details : " + details)
print("menu info: " + menu_info)
print("menu description : " + menu_decrtiption)
print("menu : " + menu_children)

#page dataframe
df = pd.DataFrame([{
    "title" : page_tittle,
    "header" : page_header,
    "headerinfo" : page_header_details,
    "details" : details,
    "menuinfo" : menu_info,
    "menudescription" : detail_menu
}])

df.to_csv("../documents/humphrey.csv")

#for item in items:
    #print(item.get_text())



#pyhton
#html
#beautifull soup
#beautifull soup methods

#when yo select you will always get a list



#Restaurant scraping

#Scrape a restaurant website and print details. You’re free to use either a terminal program or a Jupyter Notebook.

#Find a restaurant website, preferably one that doesn’t have a lot of dynamic content using Javascript. Try to scrape the site for the restaurant where you had dinner most recently.
#Save a page to a html file
#In a comment in your Notebook include the URL that you saved
#Load the HTML file using BeautifulSoup
#Get the <title> element and at least two other elements from the page.
#Try to get as other elements from the site using scraping.
#Make sure to also upload the html file to Github!
#Tips

#Take a look at the example.
#Check if you have BeautifulSoup by running a Python console and executing from bs4 import beautifulsoup
#If that doesn’t work you need to do pip install beautifulsoup4 from the terminal or the Anaconda Prompt
#Maybe you can use a function to simplify repeating tasks, like getting the first elements text after doing .select()
#Extended exercise

#Scrape the restaurants menu and save that to a CSV or JSON file using Pandas