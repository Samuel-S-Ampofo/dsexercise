import requests
import json

user_text = input("type here what you want to search on wikipedia : ")
user_text = user_text.split(' ')

user_search = '_'.join(map(str,user_text)).title()
search_link = f'https://en.wikipedia.org/api/rest_v1/page/summary/{user_search}'
nl_search_link = f'https://nl.wikipedia.org/api/rest_v1/page/summary/{user_search}'
zh_search_link = f'https://es.wikipedia.org/api/rest_v1/page/summary/{user_search}'

serach_list = [search_link,nl_search_link,zh_search_link] 

#search link
for link in serach_list:
	req_rturn = requests.get(link)

	if req_rturn.status_code != 200:
			print("oops you have a back network thing here")
			exit()
	#loading wiki json dat
	search_data = json.loads(req_rturn.text)
	nl = "\n"

	for key in search_data:
		article_tittle = search_data["title"]
		article_description = search_data["description"]
		article_extract = search_data["extract"]
	print(f'{nl}')
	print("------------ Hers is the text from your wiki search ------------")
	print(f'{nl}{nl}Tittle: {article_tittle}{nl}{nl}Description: {article_description}{nl}{nl}Extract: {article_extract}')