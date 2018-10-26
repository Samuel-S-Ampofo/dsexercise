def convert_euros(amount,currency):
	if currency == "pound":
		return amount * 0.88311
	elif currency == "yen": 
		return amount * 128.487
	elif currency == "dollar":
		return amount * 1.14590
	else:
		return "sorry your currenecey is not listed"

print(convert_euros(12, "pound"))
print(convert_euros(43, "yen"))
print(convert_euros(9.32, "dollar"))
print(convert_euros(5, "oreo"))
