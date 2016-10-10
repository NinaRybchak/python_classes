import math

def polysum(n, s):
	area = (0.25 * n * (s**2)) / math.tan(math.pi / n)
	perimeter = n * s
	return round(area + perimeter**2, 4)

n = int(input("Enter number of sides: "))
s = float(input("Enter lengh of sides: "))
print("Result is {}".format(polysum(n,s)))