#!/usr/bin/python3
#-*-coding:utf-8 -*-

#生成器无法重复使用，但是可以创建一个对象，讲它的__iter__方法调用得到一个生成器

class Counter(object):
	def __init__(self, low, high):
		self.low = low
		self.high = high
	
	def __iter__(self):
		counter = self.low
		while self.high >= counter:
			yield counter
			counter += 1


gobj = Counter(5, 10)
for num in gobj:
	print(num, end=' ')

for num2 in gobj:
	print(num, end=' ')


'''
# 生成器举例

def my_generator():
	print("Inside my generator")
	yield 'a'
	yield 'b'
	yield 'c'

for char in my_generator():
	print(char)


print(' ')
print('用生成器函数完成与Counter类相同的功能')
def counter_generator(low, high):
	while low <= high:
		yield low
		low += 1

for i in counter_generator(5, 10):
	print(i, end=' ')
'''

'''
迭代器举例

class Counter(object):
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		#返回下一个值知道当前值大于high
		if self.current > self.high:
			raise StopIteration
		else:
			self.current += 1
			return self.current

c = Counter(5, 10)
for i in c:
	print(i, end=' ')

print(' ')
print('-' * 20)

a = Counter(6, 10)
iterator = iter(a)

while True:
	try:
		x = iterator.__next__()
		print(x, end=' ')
	except StopIteration as e:
		break
'''

