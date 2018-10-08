
import json 

# assignment
my_movie = {"title": "The Lord of the Rings",
		    "year": "2001",
		    "duration":192,
		    "director ":"Peter Jackson",
		    }

for key in my_movie:
	if my_movie[key] == "duration":
		value = f"{value} munites"
	print(key, my_movie[key])

# 
movie_tittle = input("what the tittle of your movie ")
movie_year = input("what the release year of your movie ")	
movie_duration = input("what the duration of your movie ")
movie_director = input("who is the director of your movie ")

movie_details ={}
movie_details.update(
		{"title": movie_tittle,
		"year": movie_year,
		"duration ":movie_duration,
		"director ":movie_director,
		})

user_string = " 	"
print("here are the details of your movvie")
print(json.dumps(movie_details,indent =4))	

