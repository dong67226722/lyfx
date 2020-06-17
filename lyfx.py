import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open("lyfx.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print("档案读取完成了，总共有", len(data), "笔资料")

print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print("留言的平均长度是：", sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("一共有", len(new), "笔资料少于100")


love = []
for d in data:
	if "love" in d:
		love.append(d)
print("一共有", len(love), "笔资料提到love")

#文字计数
start_time = time.time()
wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了',end_time - start_time, '秒')
print(len(wc))


while True:
	word = input('请输入要查询的字：')
	if word == 'q':
		break
	if word in wc:
		print(word ,'出现的次数为：', wc[word])
	else:
		print('你查的字没有出现过！')

print('感谢使用查询功能！')




