
import json

with open("../documents/movies.json") as json_file:
    json_data = json.load(json_file)

user_movie = input("Type a year movie you are looking for ")
user_movie = int(user_movie)

# serach for movie by years i wrote a simple fuction for this
def movie_search(userinput,moviedata):
	for movie in moviedata:
		if userinput == movie["year"]:
			print(json.dumps(movie,indent =4))

movie_search(user_movie,json_data)


#movie filter
print("Now let's choose a movie based on your options"+"\n"
	  +"1: Movies by tittle"+"\n"
	  +"2: Actors name"+"\n" 
	  +"3: Maximum munites of movies you want to see "+"\n" 
	  +"4: The directors who movie you wnat to see"+"\n")


#filter options and to string
user_filter_type = input(" type in one of the above options to search by:")
user_filter_type = int(user_filter_type)


#useroptions
if user_filter_type == 1:
	user_query = input("Type tittle so search movie by tittle ")

if user_filter_type == 2:
	user_query = input(" Type actors name to serach movie actors ")

if user_filter_type == 3:
	user_query = input(" Type the maximum munites of movies you want to see ")

if user_filter_type == 4:
	user_query = input("Type directors name to serach movie actors ")


#user filter using a a function
def movie_filter(searchtype,userinput,moviedata):
	if searchtype == 1:
		for movie in moviedata:
			if userinput == movie["title"]:
					print(json.dumps(movie,indent =4))
	if searchtype == 2:
		for movie in moviedata:
			if userinput in movie["actors"]:
					print(json.dumps(movie,indent =4))
	if searchtype == 3:
		for movie in moviedata:
			movie["duration"] = str(movie["duration"])		
			if userinput <= movie["duration"]:
					print(json.dumps(movie,indent =4))
	if searchtype == 4:
		for movie in moviedata:
			if userinput == movie["director"]:
					print(json.dumps(movie,indent =4))
			
movie_filter(user_filter_type,user_query,json_data)

