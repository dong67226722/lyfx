data = []
count = 0
with open("lyfx.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 2000 == 0:
			print(len(data))
print("档案读取完成了，总共有", len(data), "笔资料")

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print("留言的平均长度是：", sum_len / len(data))