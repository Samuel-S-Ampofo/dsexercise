#refactoring, PPrint module,jason module, panda	
my_friends = { "John",
			   "Emmanuel",
			   "Jame"
			 }

for friend in my_friends:
	snack_name = input(f'what is the favorite snack of {friend} ')
	print(f" {friend} like {snack_name }")
	my_friends.update({friend:{"cookies":snack_name}})
