'''
Write two Python functions to find the minimum number in a list. The first function should
compare each number to every other number on the list. O(n 2 ). The second function should be
linear O(n).
'''
import random
import time
import math
start = time.time()

def min_num_1(num_list): #O(n2) complexity
	for number_1 in num_list:
		min_num = number_1
		flag = True

		for number_2 in num_list:
			if number_2 < min_num:
				flag = False

		if flag  == True:
			return min_num

def min_num_2(num_list):
	min_num =  num_list[0]
	for i in num_list:
		if i < min_num:
			min_num = i 
	return i

def main():
	 random_num = random.sample(xrange(1, 1000000), 100000)
	 print(min_num_1(random_num))
	 print(min_num_2(random_num))

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))



