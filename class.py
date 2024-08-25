class student():
    age = 24
    edu_year = "Last Year"
    stream = "computer"
    college_name = "sits"
    location = "pune"


sambhaji = student()

print(sambhaji.edu_year)


class programmer():
    company = "google"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

emp1 = programmer("sambhaji",4200000)
print(emp1.company,emp1.name,emp1.salary)

emp2 = programmer("raja",2000000)
print(emp2.company,emp2.name,emp2.salary)

emp3 = programmer("gita",5600000)
print(emp3.company,emp3.name,emp3.salary)





# self




class greet():
    def hello(self):
        print("good morning sambhaji")

ram = greet()

ram.hello()


# init method  = constructor



class student():
    def __init__(self,age,edu_year,stream):
        self.age =  age
        self.edu_year = edu_year
        self.stream = stream 
        print("all done")

radhe = student(23,4,"comp")

print(radhe.stream)