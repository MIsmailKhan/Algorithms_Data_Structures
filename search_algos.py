class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)

	def hash_function(self,key,size):
		return key % size	

	def rehash(self,old_hash,size):
		return (old_hash + 1) % size

	def put(self,key,data):
		hash_value = self.hash_function(key,len(self.slots))

		if self.slots[hash_value] == None:
			self.data[hash_value] = key
			self.data[hash_value] = data
		else:
			if self.slots[hash_value] == key:
				self.data[hash_value] = data #replace
			else:
				next_slot = self.rehash(hash_value,len(self.slots)) 
				while self.slots[next_slot] != None and self.slots[next_slot] != key: 
					next_slot = self.rehash(next_slot,len(self.slots))

				if self.slots[next_slot] ==  None:
					self.slots[next_slot] = key
					self.data[next_slot] = data
			  	else:
			  		self.data[next_slot] = data #replace

	def get(self,key):
		start_slot = self.hash_function(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = start_slot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots))
				if position == start_slot:
					stop = True
		return data
				
		

def sequential_search(a_list, item):
	pos =  0 
	found = False

	while pos < len(a_list) and not found:
		if a_list[pos] == item:
			found = True
		else:
			pos += 1

	return found, pos

def ordered_sequential_search(a_list,item):
	found = stop = False
	pos = 0

	while pos<len(a_list) and not found and not stop:
		if a_list[pos] == item:
			found  = True
		elif a_list[pos] > item:
			stop = True
		else:
			pos += 1

	return found,pos

def binary_search(sorted_list,item): # O(log n)
	first = 0
	last = len(sorted_list) - 1
	found =  False
	while first<=last and not found:
		mid = (first + last)//2
		if sorted_list[mid] == item:
			found = True
		elif sorted_list[mid] < item:
			first = mid + 1
		elif sorted_list[mid] > item:
			last = mid - 1
		else:
			pass

	return found, mid

def binary_search_recursive(sorted_list,item):
	if len(sorted_list) == 0:
		return False
	else:
		mid  = len(sorted_list)//2
		if sorted_list[mid] == item:
			return True,mid
		elif sorted_list[mid] > item:
			return binary_search_recursive(sorted_list[:mid - 1],item)
		else:
			return binary_search_recursive(sorted_list[mid + 1:],item)

def hash(a_string, table_size):
	sum = 0
	for pos in range(len(a_string)):
		sum += ord(a_string[pos])
	return sum%table_size


'''
test_list = [1,2,32,8,17,42,13,0]
print(sequential_search(test_list,3))
print(sequential_search(test_list,13))

test_list_2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list_2, 3))
print(ordered_sequential_search(test_list_2, 13))

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search_recursive(test_list, 3))
print(binary_search_recursive(test_list, 13))
'''

h=HashTable()
h[54]="cat"
h[26]="dog"
h[93]="lion"
h[17]="tiger"
h[77]="bird"
h[31]="cow"
h[44]="goat"
h[55]="pig"
h[20]="chicken"
print(h.slots)
print(h.data)
