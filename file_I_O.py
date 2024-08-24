
#read data form file 


f = open("file.txt")    #select file to read data

data = f.read()         # access data from file to another variable

print(data)             # print data
f.close()               # close open file


#write data inside the file 

new_data = "my qualificition is computer engineer"              #add this data inside file


f = open("file.txt" , "w")                                          #open file in write mode

data = f.write(new_data)                                        #give data to add inside file
f.close()                                                        





