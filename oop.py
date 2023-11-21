class Travel:                                  # class name
    def bus(self):
        print("40 pasanger")

    def car(self):
        print("4 pasanger")


travel  = Travel                               # object "instance of the class"
Travel.bus(travel)                             # call class
Travel.car(travel)                             # call class



class School:
    def __init__(self):                        # init method call itself
        print("total no of student: 50")

    def boys(self):
        print("30 boys in school")

    def girls(self):
        print("20 girls in school")


school = School
School()                                        # call class

# inheretance in python

class A:
    def program1(self):
        print("sambhaji is here")
        a = 5
        b = 6

class B(A):
    def program2(self):
        print ("prasad is here")

a1 = A()
b1 = B()


a1.program1()
b1.program1()
b1.program2()