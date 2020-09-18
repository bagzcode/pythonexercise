number = int(input())
count = 1
total = 0
neg = 0
print("number","count","temp","total","neg")
while count <= number:
	temp = int(input())
	if temp >= 20:
		total += temp
	if temp <= 0:
		neg += 1
	count +=1
	print(number,count,temp,total,neg)


print(total, neg)