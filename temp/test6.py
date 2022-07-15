
i = ""
a = []
s = 0

while True:
	i = input("number = ")
	if (i == "q"):
		break
	# check if x is an integer
	x = int(i)
	a.append(x)
	s = s + x

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


