import time
import math
start = time.time()

# Time complexity is O(2*NlogN + N) , sorting + iterating through list once
# Brute force is N! time complexity

def anagram_solution2(s1,s2):
	a_list1 = sorted(list(s1))
	a_list2 = sorted(list(s2))
	
	
	pos = 0
	matches = True
	while pos < len(s1) and matches:
		if a_list1[pos] == a_list2[pos]:
			pos = pos + 1
		else:
			matches = False

	return matches
	
def main():
	print(anagram_solution2('abcde','edcba'))


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))