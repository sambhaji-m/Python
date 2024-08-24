def greet(user):
    print(f"hello {user}")

greet(input("enter user name: "))


# program to calculate values

def calculate(a,b):
    x = a + b
    print(f"final calculated value is {x}")


a = int(input("enter value for calculation: "))
b = int(input("enter value for calculation: "))

calculate(a,b)