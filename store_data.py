#opening files for users  and writing
#reading users file and  and print to screen
file_route = "../documents/politicians.csv"
politician_details = open(file_route, "r")

# write politicians to list
politician_list = []
for politician in politician_details:
	clean_str = politician[0:-1]
	each_politician_list = clean_str.split(",")
	politician_list.append(each_politician_list)
politician_details.close()

# a simple fuction to ead the list at any ghiven time
def read_list(user_list):
	user_list = user_list[0:-1]
	print("-"*10 +" here is your new list with index" + "-"*10 )
	print("\n")
	for user in user_list:
		user_index = user_list.index(user)
		print(f'{user_index} : {user[0]} {user[1]} was born in  {user[2]} and a memeber of {user[3]} political party ')
	print("\n")

#remove user from the list and get it printed back with index of list
def remove_action(user_index,user_data):
	user_data.remove(user_data[user_index]);
	read_list(user_data)

def save_action(user_data,file_path):
	#unkn_list = [" "]
	write_user = open(file_path, "w")
	for user in user_data:
		user_info =   ','.join(map(str, user))+"\n"
		print(user_info)
		write_user.write(user_info)
	write_user.close()


#user option and wrting to file
# while loop for user to choose options untile QUIT
action_status = " "
while action_status !="quit":
	read_list(politician_list)
	print("\n" )
	print("Now here are some options "+"\n" 
	      +"1: type REMOVE to delet a politition form the list "+"\n"
		  +"2: tyepe ADD to add apolition to the list"+"\n" 
		  +"3: type SAVE to save current list to csv "+"\n" 
		  +"4: tye READ to read the program"+"\n"
		  +"4: tye QUIT to end th program"+"\n")

	#taking user details
	user_action = input("type in one of the above options to exercute: ")
	user_action = user_action.lower()
	action_status=user_action

	if user_action == "add":
		politician_list = politician_list[0:-1]
		unkn_list = [" "]
		first_name = input("type in politician first name: ")
		first_name = first_name.lower()
		last_name = input(" type in polititions last name: ")
		last_name = last_name.lower()
		date_of_birth = input(" type in polititions year of birth: ")
		date_of_birth = int(date_of_birth)
		pol_party = input(" type in polititions party : ")
		pol_party = pol_party.lower()
		new_politician_info = [first_name,last_name,date_of_birth,pol_party]
		politician_list.append(new_politician_info)
		politician_list.append(unkn_list)
	read_list(politician_list)

	if user_action == "remove":
		pol_index = input(" type in the index polititions you want to remove: ")
		pol_index  = int(pol_index)

		print(f" removing... polititian   with the index {pol_index}")
		remove_action(pol_index,politician_list)

	if user_action == "save":
		save_action(politician_list,file_route)

	if user_action == "read":
		unkn_list = [" "]
	read_list(politician_list)

		


