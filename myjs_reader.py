
import json

with open("../documents/movies.json") as json_file:
    json_data = json.load(json_file)

user_movie = input("Type a year movie you are looking for")
user_movie = int(user_movie)


#for movie in json_data:
	#if user_movie == movie["year"]:
		#print(json.dumps(movie,indent =4))


def movie_search(userinput,moviedata):
	for movie in moviedata:
		if userinput == movie["year"]:
			print(json.dumps(movie,indent =4))

movie_search(user_movie,json_data)


#print(json.dumps(json_data,indent =4))
