guess = 9
count = 0
limit = 3
while count < limit:
    no = int(input("enter the no for guessing "))
    if no == guess:
        print("You Won")
        break
    count = count+1
else:
    print("You faild! try next time")

    