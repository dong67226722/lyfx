data = []
with open("lyfx.txt", "r") as f:
	for line in f:
		data.append(line)
print(len(data))

print(data[3])