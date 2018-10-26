
import requests
import json
import pprint 


user_details  = {
					"search_info":{"ex_market":[],
								   "assets":[]
									 }
								   }
n_line = "\n"

print("hey ! Bit investor welcome to a wonderfull trading day lets atrt with some basics")

user_name = str(input("what's your full  name : "))
user_adress = str(input("your adress : "))
user_budget = int(input("how much do budget to invest in crypto currenecy : "))
user_email = str(input("whats you e-mails : "))
user_details.update({
	                  "user_name":user_name,
	                  "user_address":user_adress, 
	                  "user_budget":user_budget, 
	                  "user_email":user_email, 

	                  })

#user confirms what he wants to on the appplication
user_confirmation = "no"
while user_confirmation == "no":
	print(f"great ! {user_name} here are some option to help you on your investment of {user_budget} TODAY !")
	user_query = str(input(f" {n_line} 1. type 'exchanges' to get all trading market {n_line} 2. type 'assets' to get an overview of all crpto currencies "))
	user_query = user_query.lower()
	user_confirmation = str(input( f"you want to search for {user_query} confirm with 'YES' or 'NO'" ))
	user_confirmation = user_confirmation.lower()


def api_request(ext_url):
	url = f'https://rest.coinapi.io/v1/{ext_url}'
	headers = {'X-CoinAPI-Key' : 'E3EC80DB-0297-44F9-A925-795C54BD4001'}
	response = requests.get(url, headers=headers)
	cypto_data = json.loads(response.text)
	return cypto_data

#whats infnluenec the market
#acess to infomations
#list all bit trading market and their makrt opening and closesing time
#link to their website
# 1.  all cryptomarket and assets
#use jupyter notebook to show a table of the top ten list on the market describe// 
pprint.pprint(api_request(user_query))

# 2. get specific crpto infomatio
# if market show a deffrent option 
#if assets a diffrenet option
if user_query == 'exchanges':
	specific_query =  input("type here the name of cryptomarket you want information on: ")
	specific_query = specific_query.upper()
	specific_x_data = api_request(user_query)
	for  item in specific_x_data:
		if item["exchange_id"] == specific_query:
			print(f"-----------here is your information on {specific_query} -----------")
			pprint.pprint(item)
		user_details["search_info"]["ex_market"].append(specific_query)

if user_query == 'assets':
	specific_query =  input(f"type here id assest you want information on {n_line} This can be found in the asset id column: ")
	specific_query = specific_query.upper()
	url_specific_query = f"exchangerate/{specific_query}"
	print( f"----------{url_specific_query}---------")
	pprint.pprint(api_request(url_specific_query))
	user_details["search_info"]["assets"].append(specific_query)

pprint.pprint(user_details)
print("Next step !!!")


#url = 'https://rest.coinapi.io/v1/exchangerate/BTC'
#headers = {'X-CoinAPI-Key' : '73034021-0EBC-493D-8A00-E0F138111F41'}
#response = requests.get(url, headers=headers)


#get exchange rates 
#url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
#headers = {'X-CoinAPI-Key' : '73034021-0EBC-493D-8A00-E0F138111F41'}
#response = requests.get(url, headers=headers)


#all excganhe rates
#url = 'https://rest.coinapi.io/v1/exchangerate/BTC'
#headers = {'X-CoinAPI-Key' : '73034021-0EBC-493D-8A00-E0F138111F41'}
#response = requests.get(url, headers=headers)



#list all periods
#url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1MIN'
#headers = {'X-CoinAPI-Key' : '73034021-0EBC-493D-8A00-E0F138111F41'}
#response = requests.get(url, headers=headers)

#hostoric data
#url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history?period_id=1MIN&time_start=2016-01-01T00:00:00'
#headers = {'X-CoinAPI-Key' : '73034021-0EBC-493D-8A00-E0F138111F41'}
#response = requests.get(url, headers=headers)

#url = 'https://rest.coinapi.io/v1/orderbooks/BITSTAMP_SPOT_BTC_USD/history?time_start=2016-01-01T00:00:00'
#headers = {'X-CoinAPI-Key' : '73034021-0EBC-493D-8A00-E0F138111F41'}
#response = requests.get(url, headers=headers)



#a data scraper and/or application that collects, cleans and 
#analyzes relevant information needed to test the hypotheses
#a visualization that interprets the data in such a way that the 
#hypotheses can be tested. The prototype has to work properly, i.e.
# has to be able to scrape data, has to deal with some regular exceptions, 
#has to collect relevant data, has to be able to clean data in an acceptable way, 
#has to be able to translate that data in an (interactive) visualization.
