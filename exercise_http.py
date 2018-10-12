import requests
import json


user_url = input("type here your url")

pre_link = "http://"
user_link = pre_link + user_url
r = requests.get(user_link)

print(user_link)

if r.status_code == 200:
	print("print you got it")
else: 
	print("oops you have a back network thing here")

for key in r.headers:
	print(key,r.headers[key])
print(r.headers)

print(json.dumps(r.headers,indent =4))

# headers part dislplay the details of the request.

#exercise: URL Checker

#create a program that asks the user for an URL, does a GET request for that URL and displays the useful information.

#import the requests library
#Ask the user for an URL and strip() it
#Check the status_code, if it is not 200, display an error and exit the program
#Loop over the headers and display the key and value of every header.
#Extend your program

#Display the first ten lines of the text of the page the user provided
#Tips

#Everything you need for this exercise is in the ‘lesson 6’ chapters of the examples-3 Jupyter Notebook.
#If you can’t import the requests library you might need to install it using the pip command line utility
#Use requests.get() to do a GET request
#The status_code is an int
#F-strings are really useful for this exercise
#Remember the .items() method of dictionaries


