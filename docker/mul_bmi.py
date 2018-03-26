#!/usr/bin/python
height=input('just like "1.83",please input your height: ')
weight=input('just like "62",please input your weight: ')
n=float(height)*float(height)
m=float(weight)/float(n)
if m<18.5:
	print('you are too thin',m)
elif m<25:
	print('you are very normal',m)
elif m<28:
	print('you are little fat',m)
elif m<32:
	print('you are very fat',m)
elif m<35:
	print('you are too fat',m)
else:
	print('error',m)
