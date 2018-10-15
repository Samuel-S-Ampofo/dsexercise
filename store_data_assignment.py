#opening files for users  and writing
#reading users file and  and print to screen
politition_list = []
politition_details = open("../documents/politicians.csv", "r")
file_route = "../documents/politicians.csv"

#fuction for reading, writting and printing a politition list
print("\n")
for poloitition in politition_details:
	new_poloitition = poloitition.split(",")
	politition_list.append(new_poloitition)

	for politition in politition_list:
		politition_stats = poloitition.split(",")
		first_name = politition_stats[0]
		last_name = politition_stats[1]
		date_of_birth = politition_stats[2]
		political_party = politition_stats[3]
		pol_number = politition_list.index(politition)
	print(f'{pol_number}:{first_name}{ last_name} was born in { date_of_birth} and a memeber of {political_party} political party')
print("\n")
politition_details.close()

# fuctions to  read add,remove save and quit program
# fuction to read and print list by index 
def read_list(user_list):
	print("\n")
	print("-"*10 +" here is your new list with index" + "-"*10 )
	for user in user_list:
		user_index = user_list.index(user)
		print(f'{user_index} : {user[0]} {user[1]} was born in  {user[2]} and a memeber of {user[3]} political party')
	print("\n")

#remove user from the list and get it printed back with index of list
def remove_action(user_index,user_data):
	user_data.remove(user_data[user_index]);
	read_list(user_data)

def save_action(user_data,file_path):
	write_user = open(file_path, "w")
	for user in user_data:
		user_info =   ','.join(map(str, user)) 
		print(user_info)
		write_user.write(user_info)
	#write_user.close()
	#read_list(user_data)



#user option and wrting to file
# while loop for user to choose options
action_status = " "
while action_status !="quit":
	print("Now here are some options "+"\n" 
	      +"1: type REMOVE to delet a politition form the list "+"\n"
		  +"2: tyepe ADD to add apolition to the list"+"\n" 
		  +"3: type SAVE to save current list to csv "+"\n" 
		  +"4: tye QUIT to end th program"+"\n")

	#taking user details
	user_action = input("type in one of the above options to exercute: ")
	user_action = user_action.lower()
	action_status=user_action

	if user_action == "add":
		first_name = input("type in politian first name: ")
		first_name = first_name.lower()
		last_name = input(" type in polititions last name: ")
		last_name = last_name.lower()
		date_of_birth = input(" type in polititions year of birth: ")
		date_of_birth = int(date_of_birth)
		pol_party = input(" type in polititions party : ")
		pol_party = pol_party.lower()
		new_poloitition_list = [first_name,last_name,date_of_birth,pol_party]
		politition_list.append(new_poloitition_list)
		read_list(politition_list)

	if user_action == "remove":
		pol_index = input(" type in the index polititions you want to remove: ")
		pol_index  = int(pol_index)

		print(f" removing... polititian   with the index {pol_index}")
		remove_action(pol_index,politition_list)

	if user_action == "save":
		save_action(politition_list,file_route)







#write_user = open("../documents/user_details.csv", "w")
#write_user.write()
#write_user.close()



#Your program must:

#Read the provided csv file and convert the data to a multidimensional list (list with lists)
#Print the contents of the list properly formatted with the index number 
#(e.g. ‘0: Mark Rutte was born in 1967 and a member of the VVD party’) and also show how many people there are in the database.
#Ask for four options: 
#remove a person, 
#add a person, save the 
#database to csv or 
#quit the program.
# ----------------------------------------------
#‘Add a person’ should ask for the same four fields that also exist in the original CSV file and add those to the list.
#‘Save the database’ should save the modified list in the same format in the original file so that whenever the program 
# is quit and run again the mutations done in the program are properly reflected in the file. Alternatively, the list should be saved whenever the user 'removes' or 'adds' a person.
#The program should indefinitely provide the four options again after an action is completed until the use chooses the 'quit the program' option.
#Your program must also:

#Be properly commented.
#Be executable using the python interpreter from the command line (e.g. ‘python assignment-2.py’) 
