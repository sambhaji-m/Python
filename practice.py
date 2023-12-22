#name = " "
#if len(name) < 3:
#    print ("name must be at least 3 char")
#elif len(name)>50:
#    print("name cam be maximum of 50 char")
#else:
#    print("name looks good! ")




brain = int(input("enter no for vaishnavi brain: "))
name = "vaishnavi"
if brain <25:
    print(name + "is lafdebaz ")
elif brain >25 and brain < 50:
    print(name + "is geleli case")
elif brain >50 and brain <75:
    print(name + "is thik thak") 
elif brain >75 and brain <85:
    print(name + "is ok ok")
elif brain >85:
    print("its not possible")
