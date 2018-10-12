
#wordlist  and spell checker
wordlist = ["africa","europe","asia","america","north-america","antarctica"]
user_word = input("in simple words give a detail descriptiont where you are from in the world eg. start with city etc.. :")
new_user_word = user_word.split(" ")

for word in new_user_word:
	if word in wordlist:
		print(word)
		print(" Warnning " + word + " is a continent that is fobbiden WRONG WORD!!! in the the list ")
