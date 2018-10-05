
#multidimentioan list friends list and cookies
# frinds list exmaple
friend1 =["John"]
friend2 =["emmanuel"]
friend3 =["james"]
friends_snacks = [friend1,friend2,friend3]


for friend in friends_snacks:
	namesnack = input("what is the favorite snack of " +" "+ friend[0]+" ")
	friend.append(namesnack) 
	print(friend[0] + " likes " + friend[1])
for friend in friends_snacks:	
    print(friend[0] + " likes " + friend[1])