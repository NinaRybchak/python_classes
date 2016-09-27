f_dish = "Soup and salad"
s_dish = "Pasta with meat sauce"
t_dish = "Chef's special"
print("1. " + f_dish + "\n"
	"2. " + s_dish + "\n"
	"3. " + t_dish + "\n")
number = input('Which number would you like to order? ')
if number == "1":
	print(f_dish + " coming right up!")
elif number == "2":
	print(s_dish + " coming right up!")
elif number == "3":
	print(t_dish + " coming right up!")
else:
	print("Sorry, that is not a valid choice.")