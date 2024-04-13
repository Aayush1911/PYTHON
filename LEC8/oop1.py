class Student:
    college='SVIT' #class Attribute
    dept='IT' #class Attribute

    # default Constructor made by python
    # def __init__(self):
    #     print('Constructor is called')

    # Parameterized contructor
    def __init__(self,name,cgpa):
        self.name=name #object Attribute
        self.cgpa=cgpa #object Attribute

    # Methods
    def welcome(self):
        print("Welcome",self.name)

s1=Student("Aayush",8)
# s1.welcome()
# print(Student.college,Student.dept,s1.name,s1.cgpa)

s2=Student('Arjun',9)
# s2.name='karan'
# print(s2.college,s2.dept,s2.name,s2.cgpa)

# take name and marks of 3 subject and calculate average with the help of method
# class s:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def average_marks(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         return sum/3
    
# st=s('Aayush',[95,96,97])
# print(st.average_marks())

# static methods
# Methods that don’t use the self parameter (work at class level)

# class a:
#     @staticmethod
#     def college():
#         print("SVIT")

# a1=a()
# a.college()

# Abstraction
#Hiding the implementation details of a class and only showing the essential features to the user.

# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.brk=True
#         self.clutch=True
#         print("Car Started")

# c1=Car()
# c1.start()
# so we see in output only car started but does not show the internal implemenatation

# Encapsulation
# Wrapping data(attributes) and functions(methods) into a single unit (object).

# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
# class Bank:
#     def __init__(self,accno,bal):
#         self.accno=accno
#         self.bal=bal

#     def debit(self,amount):
#         self.bal-=amount
#         print("Rs",amount,"was debitted")

#     def credit(self,amount):
#         self.bal+=amount
#         print("Rs",amount,"was credited")

#     def getbalance(self):
#         print('Total Balance is',self.bal)

# b=Bank(1258,5000)
# b.debit(500)
# b.getbalance()
# b.credit(1000)
# b.getbalance()