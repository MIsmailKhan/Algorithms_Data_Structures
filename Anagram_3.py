import time
import math
start = time.time()
# Solved in linear time O(N)

def anagram_solution4(s1, s2):
	c1 = [0] * 26
	c2 = [0] * 26

	for i in range(len(s1)):
		pos = ord(s1[i]) - ord('a')
		c1[pos] += 1

	for i in range(len(s2)):
		pos = ord(s2[i]) - ord('a')
		c2[pos] +=  1

	j = 0
	still_ok = True
	while j < 26 and still_ok:
		if c1[j] == c2[j]:
			j = j + 1
		else:
			still_ok = False

	return still_ok


def main():
	print(anagram_solution4('apple','pleap'))


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))