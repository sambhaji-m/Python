import random

n = random.randint(1,100)

guess_count = 0

no = -1

while no != n:
    guess_count +=1
    a=no = int(input("enter number for guess: "))
    if a>n:
        print("lower no pls")

    else:
        print("higher number pls")\
        
print(f"you guess correct number in {guess_count} counts")