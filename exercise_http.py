import requests
import json

user_url = input("type here your url : www.")

user_link = "http://" + user_url
req_rturn = requests.get(user_link)

if req_rturn.status_code != 200:
	print("oops you have a back network thing here ")

print(f"Here are the details of your website :{user_link}")
	
for key in req_rturn.headers:
	print(f'{key} : {req_rturn.headers[key]}')
print("------------ Hers is the text from your website ------------")
print(req_rturn.text.split("\n")[0:10])


