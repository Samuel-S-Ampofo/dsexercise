
import json 

footballers_doc = open("../documents/footballers.csv", "r")

write_footballer = open("../documents/new_footballers.csv", "w")
footballers_details ={}

for foootballer in footballers_doc:
	players_info = foootballer.split(",")
	player_name = players_info[0]
	Player_club = players_info[1]
	player_worth = players_info[2]

	footballers_details.update(
		{"player_name": player_name,
		"player_club": Player_club,
		"players_worth":player_worth
		})

	write_footballer.write(footballers_details["player_name"] + " plays for " +
		  footballers_details["player_club"] + " and was bought for " + 
		  footballers_details["players_worth"] + "million"
		 )
footballers_doc.close()


