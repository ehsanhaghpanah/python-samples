
x = "0"
a = []
s = 0

while x != "q":
	x = input("number = ")
	if (x == "q"):
		break
	# check if x is an integer
	a.append(int(x))
	s = s + a

avg = s / a.count()

print(f"avg = {avg}")
l = 0
g = 0
for i in a:
	if i <= avg: 
		l += 1
	else:
		g += 1

print(f"lesser than = {l}")
print(f"greater than = {g}")


