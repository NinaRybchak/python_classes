soup = "Soup and salad"
pasta = "Pasta with meat sauce"
special = "Chef's special"
print("1. {} \n2. {} \n3. {}\n".format(soup, pasta, special))
number = input('Which number would you like to order? ')
if number == "1":
	print("{} coming right up!".format(soup))
elif number == "2":
	print("{} coming right up!".format(pasta))
elif number == "3":
	print("{} coming right up!".format(special))
else:
	print("Sorry, that is not a valid choice.")
