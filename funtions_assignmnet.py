import requests
import json
import pprint

# imprt ipython module for html and image

#user query and information formating
user_text = input("type here what you want to search on wikipedia : ")
user_text = user_text.split(' ')
user_lang = input("type the language in which you want the article:")
user_lang = user_lang.title()
user_search = '_'.join(map(str,user_text)).title()
user_variable = input("what do you want from the article eg.  e.g  description, extract ...")
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
	returns
	for key in search_data:
		article_desktop = search_data["content_urls"]["desktop"]["page"]
			
		if  key == user_variable:	
			article_searched = search_data[user_variable]
			print(f'{nl}')
			print(f"------------ Here is the text from your {user_variable}  on {user_search} in {user_lang}------------")
			print(f'{nl}{nl}{user_variable}: {article_searched}')
	print(f" here is your desktop url: {article_desktop}")

article_search(user_search,json_data,user_lang)



#Look at the wikifunction-skeleton.py file on how to access the Wikipedia API.
#Transform the API call to a function that accepts a title and value argument.
#Return different data, depending on what kind of value you get.
#Ask the user for title and value. Remember to clean up user input using strip(). 
#Call the function and assign the new data to a variable.
#Print the returned data
#Tips

#Note that a return statement can be used together with the if statement
#Extended exercise

#Add the option to print the desktop url of the article.
#Split your function in two functions: one that handles the API call, one that handles returning the correct data.