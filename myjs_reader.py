
import json

with open("../documents/movies.json") as json_file:
    json_data = json.load(json_file)

user_movie = input("Type a year movie you are looking for ")
user_movie = int(user_movie)

# serach for movie by years
def movie_search(userinput,moviedata):
	for movie in moviedata:
		if userinput == movie["year"]:
			print(json.dumps(movie,indent =4))

movie_search(user_movie,json_data)


#movie filter
print(" now let's choose a movie based on your options"+"\n"
	  +"1:longer than a certain duration 120 munites "+"\n"
	  +"2:director is also an actor"+"\n" 
	  +"3: search for a movie by tittle"+"\n" 
	  +"4:directed by a specific director"+"\n")

user_filter_option = str(input(" type here an option"))
user_filter_info = input(" type here an seacrh info")

def movie_filter(userinput,moviedata):
	for movie in moviedata:
		if userinput in movie["actors"]:
			print(json.dumps(movie,indent =4))
		if userinput > movie["year"]:
			print(json.dumps(movie,indent =4))
		if userinput == movie["year"]:
			print(json.dumps(movie,indent =4))
		if userinput == movie["year"]:
			print(json.dumps(movie,indent =4))

		

movie_filter(user_filter_info,json_data)




#Extend your program

#When you print the duration of the movie, print the number plus minutes(e.g. ‘117 minutes’) instead of just the number
#Add a new key called actors with a list of actors, and when you get to this list in your loop, join them together as a string
#Tips

#Everything you need for this exercise is in the first two chapters of the examples-3 Jupyter Notebook.
#Remember that accessing a key in a dict works the same as with a list
#Exercise: movie database

#Create a program that reads the provided movies.json file, asks for a year, and displays all movies that are from that year.

#Import the json library
#Ask the user for a year
#Open the provided movies.json file and read the contents to a new variable using json.load()
#Loop over the movies and display them only if they are released in the year provided by the user.
#Extend your program

#Provide the user with other filtering options, such as:
#Movies longer than a certain duration
#Movies where the director is also an actor
#Movies that where directed by a specific director
#Be creative and think of other ways of filtering the data
