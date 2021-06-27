data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(len(data))

sum_len = 0
for li in data:
	sum_len += len(li)

print('留言平均長度為',sum_len/len(data))

	


	
