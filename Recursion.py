import math
import time
start = time.time()

# Import Stack
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

def add_list(numbers_list):
	if len(numbers_list) == 1:
		return numbers_list[0]
	else:
		return numbers_list[0] + add_list(numbers_list[1:])

def int_to_string(number,base):
	convert_string = "0123456789ABCDEF"
	if number < base:
		return convert_string[number]
	else:
		return int_to_string(number/base,base) + convert_string[number%base]

def rev_string(input): # Self Check
	if len(input) == 1:
		return input 
	else:
		return input[-1] + rev_string(input[:-1])
 
def rev_list(input_list): #Programming exercises
	if len(input)list == 1:
		return input_list[0] 
	else:
		return input_list[-1] + rev_string(input_list[:-1])

def is_palindrome(input): #lazy approach
	return input  == rev_string(input)


r_stack = Stack()
def to_str(n,base):
	convert_string = "0123456789ABCDEF"
	while n > 0:
		if n < base:
			r_stack.push(convert_string[n])
		else:
			r_stack.push(convert_string[n%base])
		n = n//base
		res = ""
		while not r_stack.is_empty():
			res += str(r_stack.pop())
	return res

# Tower of Hanoi: Using 3 stacks

class TowerOfHanoi:
     def __init__(self, numDisks):
         self.numDisks = numDisks
         self.towers = [Stack(), Stack(), Stack()]
         for i in range(n, -1, -1):
             towers[0].push(i);
 
    def moveDisk(src, dest):
         towers[dest].push(towers[src].pop())
 
    def moveTower(n, src, spare, dest):
        if n == 0:
            moveDisk(src, dest)
        else:
            moveTower(n-1, src,dest, spare)
            moveDisk(src, dest)
            moveTower(n-1, spare, src, dest)

# Now that you have seen the code for both moveTower and moveDisk, you may be wondering
# why we do not have a data structure that explicitly keeps track of what disks are on what poles.
# Here is a hint: if you were going to explicitly keep track of the disks, you would probably use
# three Stack objects, one for each pole. The answer is that Python provides the stacks that we
# need implicitly through the call stack.

def move_disk(fp,tp):
	print("moving disk from",fp,"to",tp)

def move_tower(height, from_pole, to_pole, with_pole):
	if height >= 1:
		move_tower(height - 1,from_pole, with_pole,to_pole)
		move_disk(from_pole, to_pole)
		move_tower(height - 1, with_pole, to_pole, from_pole)

move_tower(3, "A", "B", "C")
print(to_str(1452,16))
print(rev_string("jackal"))
print(is_palindrome("kayak"))





print(add_list([4,56,547,56512,312]))