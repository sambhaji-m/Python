n = int(input('enter no that you want to check: '))

for i in range(2,n):
    if (n%i) ==0:
        print("its not a prime no")
        break

else:
    print("its a prime number")

