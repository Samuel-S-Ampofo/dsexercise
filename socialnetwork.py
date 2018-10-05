#setup
import datetime
import json 

wkly_val_adv = 500
now = datetime.datetime.now()
my_familyname = "ampofo"
current_year = now.year
user_minage = 18
user_details ={
}

#userdaitails setup firstname
print("hey!!! Buddy welcome to e-buddy"+ "\n" + "let get you setup so you can to connect with you buddies online")
user_firstname = input(" let's begin with your first name ")
firstname_lower = user_firstname.lower()
user_details.update({"first_name" : firstname_lower })
print ( " hey !! " + user_details["first_name"] + " great to have you on e-budy")

#userdaitails setup lasttname and comparis to my last name
user_lastname = input(" what's your last name  " + user_details["first_name"] + " ")
lastname_lower = user_lastname.lower()
user_details.update({"user_lastname" : lastname_lower})
if user_lastname == my_familyname:
	print ( " it's a coincedence " + user_details["first_name"] + " we share the same family name")

#user birthdate and calculation
user_dob = input(" what's your year of birth " + user_details["first_name"] + " ")
user_dob_int = int(user_dob)
user_curr_age = current_year - user_dob_int

user_details.update({"user_lastname" : lastname_lower})
if user_curr_age < user_minage:
	print ( " SORRY" + user_details["first_name"] + " e-buddy is only for people who are 18 + ")
	quit()
else:
	user_details.update({"user_year" : user_dob_int})
	user_details.update({"user_age" : user_curr_age})

#user age value detemined
#under 35 get 30 and 36 and over get awarded 20 point
if user_curr_age <= 35:
 	user_details.update({"user_age_value" : 30})
else :
	user_details.update({"user_age_value" : 20})

#userdaitails setup lasttname and comparis to my last name
user_gender = input(" what's your gender  " + user_details["first_name"] + " male or female ")
user_gender_lower = user_gender.lower()
user_details.update({"gender" : user_gender_lower})
print( " you are " + user_details["gender"])

if user_gender_lower <= "female":
 	user_details.update({"user_gender_value" : 2})
else :
	user_details.update({"user_gender_value" : 1 })

print(user_details["user_gender_value"])


#user birthdate and calculation
internet_profile = input(" how many hours do you averagely spend online per day for social connection " + user_details["first_name"] + " ")
internet_profile_int = float(internet_profile)
int_pro_wkly = round(internet_profile_int * 7)
user_details.update({"internet_profile-weekly" : int_pro_wkly})
print("your weekly average hours online  for social connection is ")

# value for advertise
#females have a factor of 2 and male beuse they have a wide scope of inflluence
#males have an influenece scope of 1
# value for advertiser is 
#age value multiplied by gender value
# plus percentage of weekly hours onlne 
gen_age_value = user_details["internet_profile-weekly"] * user_details["user_gender_value"]
internet_pro_per = round(user_details["internet_profile-weekly"])
user_weekly_score = gen_age_value + internet_pro_per
user_weekly_value = round(user_weekly_score/100 * wkly_val_adv)
user_details.update({"user_weekly_value" : user_weekly_value})
user_value_str = str(user_details["user_weekly_value"])

print("great to have you on e-buddy " + user_details["first_name"]+
	"\n"+ " you weekkly value is " + user_value_str + " €"
	+ "\n"+" here are you user prpfile details" )

print(json.dumps(user_details,indent =4))
print("enjoy the rest of you day " + user_details["first_name"]+" see you on e-buddy again soon !! ")


