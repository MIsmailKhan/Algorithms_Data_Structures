import time
import math
start = time.time()

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


def divide_by_2(dec_number):
	rem_stack = Stack()

	while dec_number > 0:
		rem = dec_number % 2
		rem_stack.push(rem)
		dec_number = dec_number // 2

	bin_string = ""
	while not rem_stack.is_empty():
		bin_string = bin_string + str(rem_stack.pop())

	return bin_string

def base_converter(dec_number, base):
	digits = "0123456789ABCDEF"
	rem_stack = Stack()
	
	while dec_number > 0:
		rem = dec_number % base
		rem_stack.push(rem)
		dec_number = dec_number // base

	new_string = ""
	while not rem_stack.is_empty():
		new_string = new_string + digits[rem_stack.pop()]

	return new_string




def main():
	print(divide_by_2(42))
	print(base_converter(25, 2))
	print(base_converter(25, 16))


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))