import time
import math
start = time.time()

 # LIFO concept
 
class Stack:
	def __init__(self):
		self.items = list()

	def is_empty(self):
		return len(self.items) == 0

	def pop(self):
		return self.items.pop()

	def push(self,item):
		return self.items.append(item)

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

def par_checker(symbol_string):
	s = Stack()
	balanced = True
	index = 0 
	while index <len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()
		index += 1

	if balanced and s.is_empty(): 
		return True
	else:
		return False

def main():
	print(par_checker('((()))'))
	print(par_checker('(()'))

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))

'''
# General Case
import Stack

def par_checker(symbol_string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False

		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False

def matches(open, close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)
'''