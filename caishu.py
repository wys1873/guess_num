import random
start=int(input('请确定范围起始值：'))
end=int(input('请确定范围结束值：'))
r=random.randint(start,end)
i=0
while(True):
	num=int(input('你猜的数字：'))
	i=i+1
	if r<num:
		print('比答案大')
	elif r>num: 
		print('比答案小')
	else:
		print('你猜对了')
		break
print('r=',r)
print('你猜了',i,'次')