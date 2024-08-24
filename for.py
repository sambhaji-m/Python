list = [10,20,30,40,50] #calculate total from list
total = 0
for i in list:
    total = i+total
print(total)

# print * according to list value

number = [5,2,5,2,2]
for i in number:
    print(i*"*")




    # program to print table of an number
    
n = int(input("enter no: "))
for i in range(1,11):
    print(f"{n} X {i} =", n*i)




# print name that start with s
l = ["sambhaji","rohan","soham","priya","rahul","saddhart"]

for i in l:
    if i[0] =="s":
        print("name start with s: ",i)

# same program using function 

for i in l:
    if i.startswith("s"):
        print("name start with s: ",i)
