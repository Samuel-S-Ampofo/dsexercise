
#name of lovers
your_name =  str(input("Enter name of person one")) 
partner_name = str( input("Enter name of person two")) 

#convert to lowercase
lover1 = your_name.lower()
lover2 = partner_name.lower()

lover_letters1 = list(lover1)
lover_letters2 = list(lover2)

#if the name are equal in lnght they get 20 points
lovepercentage =[]
if len(lover1) == len(lover2):
   lovepercentage.append(20)

#comparing charactors in words and assignnmning 10 fo each marks
for letter in lover_letters1:
  if letter in lover_letters2:
  	lovepercentage.append(10)

#diffrnce in names lenght to negative ans subtracted from total
name_diff = abs(len(lover_letters1) - len(lover_letters2))
lovepercentage.append(name_diff * -1)

#user feed back informations
total_score = sum(lovepercentage)
ranking_value = int(total_score/10)
new_total_score = str(total_score)
message = "hello lover birds "+ lover1 + " & " + lover2+ "\n"+ " your love match score is "

#lover calculator machine calculator 
if ranking_value <=0 :
	print( message + new_total_score +"% " +"this is not meant to be forget it")
elif ranking_value == 1:
	print(  message + new_total_score +"% " +"this will not work")
elif ranking_value == 2:
	print(message + new_total_score +"% " +"this has minimale chance")
elif ranking_value == 3:
	print( message+ new_total_score +"% " +"maybe you want you can try")
elif ranking_value == 4:
	print( message + new_total_score +"% " +"this might not work maybe")
elif ranking_value == 5:
	print( message+ new_total_score +"% " +"this  can work if you both  wantt it")
elif ranking_value == 6:
	print( message + new_total_score +"% " +"this will work will withabit commitement too ")
elif ranking_value == 7:
	print( message + new_total_score +"% " +"this will definatley work out")
else :
	print( message + new_total_score +"% " +"this is meant to be give it all you can")
