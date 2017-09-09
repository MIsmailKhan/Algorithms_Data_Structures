import time
import math
start = time.time()

# FIFO concept

class Queue:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return len(self.items) == 0 
	def enqueue(self,item):
		return self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)

def hot_potato(name_list, num):
	sim_queue = Queue()
	for name in name_list:
		sim_queue.enqueue(name)
	while sim_queue.size() > 1:
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())
		sim_queue.dequeue()
	return sim_queue.dequeue()

def main():
	q = Queue()
	q.enqueue('hello')
	q.enqueue('dog')
	q.enqueue(3)
	q.dequeue()
	print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 7))


elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))
