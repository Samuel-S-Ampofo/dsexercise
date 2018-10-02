
#imprt jason here 
import json 
num_cookies = float(input("Hey fitness  pal how many chocolate Cokies did you had today "))
num_cookies = int(num_cookies)

#calories per cooky
calorie = 75
fat = 3 
cholesterol = 0 
carbohydrates =12 
fiber = 1.5 
protein = 1.5 

# calories calculation
amount_cookies = str(num_cookies)
new_calorie = 75 * num_cookies
new_fat = 3 * num_cookies
new_cholesterol = 0 * num_cookies
new_carbohydrates =12 * num_cookies
new_fiber = 2 * num_cookies
new_protein = 2 * num_cookies


#cokkie dictionary
cookie_calories = {
  "Calories": new_calorie,
  "Fat": new_fat,
  "Cholesterol": new_cholesterol,
  "Carbohydrates":new_carbohydrates,
  "Fiber": new_fiber,
  "Protein": new_protein
}

#print commands
print("Hey fittnes pal today you had " + " " + amount_cookies + " Chocolate cookies this is equivalenet to " )
print(json.dumps(cookie_calories,indent =4))