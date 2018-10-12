import requests
import json

#get a user inpute
#get the request
#loads the json
#json becomes the dicttioanary
#find the lanuguage and display the various languages type.
#check for errors 404

# display exmaple images in jupyta notebook
#wikipedia action api
# rest #https://en.wikipedia.org/api/rest_v1/page/summary/Amsterdam



#Exercise: Wikipedia extracts

#Create a program that asks for the name of an article and uses the Wikipedia REST API to get the short description and extract of that article.

#Import the requests and json libraries
#Ask the user for an article and strip it and replaces the spaces with underscores (_)
#Format the API endpoint with the article
#Use requests.get() to get the data
#Check if we got a 200 status code, otherwise abort the program
#Display the title of the article, description and extract
#Extend your program

#Instead of just showing the description and extract in one language, show it in three languages of your choice.  For a list of all Wikipedia language editions with their respective codes ('en', 'es', 'nl', etc.) check this list.
#Look at the JSON output in a webbrowser, maybe you can display more interesting properties (for example, latitude and longitude).
#Tips

#Everything you need for this exercise is in the ‘lesson 6’ chapters of the examples-3 Jupyter Notebook.
#Use the replace() method to replace spaces with strings.
#Use json.loads() to convert the text of the GET request to a dictionary
#Assigning the dictionary values to a variable (e.g. extract = data["extract"]) is handy here.
#Again, F-strings are very useful in this program