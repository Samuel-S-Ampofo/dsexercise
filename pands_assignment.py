#pandas methods
#panda module eg csv, json ...
import pandas as pd
df = pd.read_csv("./temperature.csv")

df.head()



#Create a new Jupyter Notebook that shows some interesting statistics about the 
#temperatures.csv file (found in the Github repo)

#Import the pandas library as pd
#Read the csv file using the read_csv() method to a new Dataframe
#************************************************
#Show the first five entries using the head() method
#Use the describe() method to show general statistics about the temperature
#Show all days where the temperature was above 22 degrees
#Show all days where the temperature was below -3 degrees
#Add a new column called freezing that contains a boolean (True or False) if the 
#temperature in that row is beneath zero degrees. Print the first ten rows.
#Use plot() to show a line chart of the temperature
#Tips

#Make sure to put your temperatures.csv file in the same directory as your notebook.
#Extended use

#When you’re done try exploring other options and functions of the pandas library.