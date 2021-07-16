import random
r=random.randint(1,100)

while(True):
	num=int(input('你猜的数字：'))
	if r<num:
		print('比答案大')
	elif r>num: 
		print('比答案小')
	else:
		print('你猜对了')
		break
print('r=',r)