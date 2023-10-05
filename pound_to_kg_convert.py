pound = int(input("enter your weight in pound: "))
kg = pound * 0.45
print(kg)

# next program

weight = int(input("enter your weight: "))
print("(L)bs or (K)g: ")
choice = input("")

if choice.upper == "L":
    convert = weight * 0.25
    print(f"you are {convert} kg")
else:
    convert = weight / 0.45
    print(f"you are {convert} pound")
