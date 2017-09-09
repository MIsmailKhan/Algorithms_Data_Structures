'''
Anagram Detection Problem: Solution 1
'''
import time
import math
start = time.time()

# Solution is of complexity: O(N^2/2 + N/2) ~ O(N^2/2)
def anagram_solution(s1,s2):
	a_list = list(s2)

	pos_1 = 0
	still_ok = True

	while(pos_1<len(s1) and still_ok):

		pos_2 = 0
		found = False
		while pos_2 < len(a_list) and not found:

			if s1[pos_1] == a_list[pos_2]:
				found = True
			else:
				pos_2 += 1

		if found:
			a_list[pos_2] = None
		else:
			still_ok = False

		pos_1 += 1

	return still_ok

def main():
	print(anagram_solution('abcd','cab'))

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))
