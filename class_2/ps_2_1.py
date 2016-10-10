def clip(lo, x, hi):
	return min(max(float(lo), float(x)), float(hi))

lo = input("lo = ")
x = input("x = ")
hi = input("hi = ")
print("Result is {}".format(clip(lo, x, hi)))
