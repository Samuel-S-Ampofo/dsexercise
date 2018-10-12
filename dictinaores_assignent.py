
import json 

# assignment
my_movie = {"title": "The Lord of the Rings",
		    "year": "2001",
		    "duration":200,
		    "director ": "Peter Jackson",
		    }

for key in my_movie:
	if key == "duration":
		my_movie[key] = f"{my_movie[key]} munites"
	print(key,my_movie[key])
#user can update the actors list in my movie and 
actors_names = input(" add actors list by names of  actors seperated by commas ")
movie_actors = actors_names.split(',')
my_movie.update({"actors":movie_actors})
print(my_movie["actors"])

for key in my_movie:
	if key == "duration":
		my_movie[key] = f"{my_movie[key]} munites"
	if key == "actors":
		my_movie[key] = ' '.join(map(str, my_movie[key]))
	print(key,my_movie[key])

print("now let's do some magic with your favorite movie")

#personal addition takes user details and print an f string with their personal movie
movie_details ={}
user_name = input("whats your name ")
movie_tittle = input("what's the tittle of your favorite movie ")
movie_year = input("what the release year of your movie ")	
movie_duration = input("what the duration of your movie ")
movie_director = input("who is the director of your movie ")

movie_details.update({"user": user_name,
		 "title": movie_tittle,
		 "year": movie_year,
		 "duration": movie_duration,
		 "director": movie_director,
		})
for key in movie_details:
	if key == "duration":
		movie_details[key] = f"{movie_details[key]} munites"
	
	print(key,movie_details[key])
print("\n")
print(f'"hey !! {movie_details["user"]} your favorite movie is {movie_details["title"]} it was realeased in {movie_details["year"]}  it last {movie_details["duration"]} and was  directed by {movie_details["director"]}')
print("\n")
print("here are the details of your movie")
print(json.dumps(movie_details,indent =4))


