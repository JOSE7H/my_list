#empty list
my_list =[]
#appending elements
my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)

# inserting value 15 at the second postion 
my_list.insert (1,15)
#extending it with [50,60,70]
my_list.extend([50,60,70])

#remove thw last element
my_list.pop()

#sorting the list in accendingn\ order
my_list.sort()

# find and print the index of the value 30
index_of_30 = my_list.index(30)
print("index of 30:", index_of_30)