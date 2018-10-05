
f = open("../documents/footballers.csv", "r")
print(f.read())


#Exercise: CSV reader
#Write a program that loads and nicely displays either the footballers.csv or paintings.csv
# file from the Github repo.

#Open the CSV file using the open() function
#Loop over the lines of the file using a for loop
#Split every line by comma (",")
#Assign the different list items to variables
#Print a nice sentence like “Interchange is a painting by Willem de Kooning and was sold for 300 million dollars”
#Close the file using the close() method
#Tips for the basic exercise

#Look at the examples-2 Notebook for more examples
#Make sure your Python file and the csv file are in the same directory
#Use the open() function with a string like this: open(“footballers.csv”)
#A file is just like a list, you can iterate using the in operator
#You will need to use the split() string method to transform a line to a list
#Note that you can assign an indexed list item to any variable for easy reference
#Make sure to close() your fil
#Advanced exercises

#Instead of printing the sentences, write them to a new text file
#Try formatting the prices to a number with the appropriate number of zeroes
#Ask for an extra footballer or painting and add that to the csv file

#friends = open("friends.txt")
#for line in friends:
	#print(line)
#f = frinds("frinds.csv")


