


#wordlist  and spell checker
wordlist = ["africa","europe","asia","america","north-america","antarctica"]
user_word = input("in simple words give a detail descriptiont where you are from in the world")
new_user_word = user_word.split(" ")
print("A detailed description of wher you are from " + user_word)

for word in wordlist:
    index = 0
    index = index + 1
    new_word = new_user_word[index]
    if new_word in new_user_word:
        print(" Warnning " + new_word+ "is a continete that is fobbiiden")

