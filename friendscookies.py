#friends list and cookies
# frinds list exmaple
myfriend = ["John","Emmanuel","Jame"]
frinds_snack = []

for name in myfriend:
    print(name)
    # print(myfriend.index(name))
    namesnack = input("what is the favorite snack of " +" "+ name+" ")
    frinds_snack.append(namesnack)
    print(name + " likes " + namesnack) 
    
for name in myfriend:
    index = 0
    index = index + 1
    snack = frinds_snack[index]
    print(name + " likes " + snack)