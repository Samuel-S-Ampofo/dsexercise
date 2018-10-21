#imprts start here
import requests
import json
import pprint

# imprt ipython module for html and image

#user query and information formating
user_text = input("type here what you want to search on wikipedia : ")
user_text = user_text.split(' ')
user_lang = input("type the language in which you want the article: ")
user_lang = user_lang.title()
user_search = '_'.join(map(str,user_text)).title()
print(f'you want to serach for {user_search} in {user_lang}')

# reading language jason// this you must privde the isonland file in you document //
with open("../documents/isolangs.json") as json_file:
    json_data = json.load(json_file)

def article_search(article,langdata,lang):
	for key in langdata:
		if  lang == langdata[key]["name"]:
			lang_code = key

	search_url = f'https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{article}'		
	print(search_url)
	req_rturn = requests.get(search_url)

	if req_rturn.status_code != 200:
			print("oops you have a back network thing here")
			exit()

	search_data = json.loads(req_rturn.text)
	nl = "\n"
	#global and local scope was a hug problem here
	article_cordinates = "sorry article has no cordinates"
	article_thumbnail = "sorry article has no thumbnail"

	for key in search_data:
		article_tittle = search_data["title"]
		article_description = search_data["description"]
		article_extract = search_data["extract"]
		if  key == "thumbnail":	
			article_thumbnail = search_data["thumbnail"]
			print(article_thumbnail["source"])
			print(article_thumbnail["width"])
			print(article_thumbnail["height"])


		if  key == "coordinates":	
			article_cordinates = search_data[key]
			print(search_data[key])
		
	print(f'{nl}')
	print("------------ Here is the text from your wiki search ------------")
	print(f'{nl}{nl}Tittle: {article_tittle}{nl}{nl}Description:{article_description}{nl}{nl}Extract: {article_extract}')
	print(f'{nl}{nl}Thumnail link: {article_thumbnail}{nl} {nl} cordinates: {article_cordinates}')

article_search(user_search,json_data,user_lang)


def related_search(related_list,langdata,lang):
	for key in langdata:
		if  lang == langdata[key]["name"]:
			rlt_lang_code =  key

	related_srch = f'https://{rlt_lang_code}.wikipedia.org/api/rest_v1/page/related/{related_list}'		
	print(related_srch)
	req_related = requests.get(related_srch)

	if req_related.status_code != 200:
			print("oops you have a back network thing here")
			exit()
	rlt_search_data = json.loads(req_related.text)
	nl = "\n"
	rlt_short = rlt_search_data["pages"][0:3]
	

	for rtl_details in rlt_short:
		for items in rtl_details:
			rtl_tittle = rtl_details["title"]
			rtl_description = rtl_details["description"]
			rtl_des_url = rtl_details["content_urls"]["desktop"]["page"]
		pprint.pprint(f'Tittle :{rtl_tittle}')
		pprint.pprint(f'Description :{rtl_description}')
		pprint.pprint(f'Destop url :{rtl_des_url}')
	print(related_list)
	print(lang)
related_search(user_search,json_data,user_lang)


#wikipedia python api module install// personal additions

#Whats your program should do:
#Your program must:
#Import the requests module and the display, Image and HTML functions from the IPython.display module
#**************************************
#Ask for the article you want to lookup on Wikipedia. 

#also ask which language you want to do query (make sure to understand how the API endpoint changes because of this)
#Confirm the article and language to the user

#Do a HTTP GET request to the Wikipedia REST Summary API (https://en.wikipedia.org/api/rest_v1/#!/Page_content/get_page_summary_title)
#Check if the HTTP request gave a 200 HTTP status code and, if so, print that your query was successful. Otherwise print an error message
#Convert the JSON data the API returns to a Python dict
#Print the returned title and description from the API request
#done here **********************************************

#Check if there’s a thumbnail, and if so, extract the thumbnail source, the html extract and 
#use the Image, HTML and display function to show those in the Jupyter Notebook. 
#If there’s no thumbnail, print an error message.
#Check if there’s a coordinate in the page, and if so, extract the ‘lat’ and ‘lon’ properties. 
#Add those to the Google Maps website (‘http://maps.google.com/?q=....’) 
#and print the URL so people can click on it. If there’s no coordinate, print an error message.
#ddo this part later here **********************************************
#Query the Wikipedia related API for articles related to the original article
#(https://en.wikipedia.org/api/rest_v1/#!/Page_content/getRelatedPages) 
#using the same methods as you did for the summary (so return an error when you don’t get a 200, etc.).
#Create a new list and from the first three related results append a dict with the title, description and url to the desktop version of the related article to that list.
#Loop through the newly created list and print every item using a nicely formatted strin g (e.g.: ‘* Article title: article description: http://en.wikipedia.org/wiki/link-to-article’)
#
#Be properly commented in the code in your notebook.
#Be executable using the Jupyter Notebook webapp. 