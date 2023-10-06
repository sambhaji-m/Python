# find largest no from list
list = [5,3,7,9,10,3,2]
largest_no = list[0] 
for i in list:
    if i > largest_no:
        largest_no = i
print(largest_no)


# using max build in function

print(max(list))

    
# remove duplicte from list 

l = [1,3,5,6,7,8,5,23,3,5,6,1,5,9]
duplicate = []
for i in l:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)
