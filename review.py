# review catch

data = []
length = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 100000 == 0:
			print(len(data))
for word in data:
	a = len(word)
	length.append(a)
print(length[0])
print(length[1])

s = 0
for a in data:
	s += len(a)  #sum = sum + len(a)
print( s / len(data))






