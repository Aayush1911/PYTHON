# del keyword
# used to delete object properties or object itself
# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student('Ajay')
# print(s1.name)
# del s1
# print(s1.name)

# private attributes and methods
# class Account:
#     __name='rajesh' #this is private attribute
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass #by placing two underscore before attribute make this as private

#     def __hello(self):
#             print("hello",self.__name)
        
#     def welcome(self):
#             self.__hello()
        
# acc1=Account('4585','abcd')
# print(acc1.acc_no)
# print(acc1.acc_pass)
# print(acc1.__name)
# acc1.welcome()  #by this way we can access private attributes and method.only internal function can access private method and attributes.

# Inheritence
# when one class(child/derived)derives the properties & methods of another class(paent/base)

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car Started")

    def stop():
        print("Car Stopped")
    
class ToyatoCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

car1=ToyatoCar("Fortuner","electric")
car2=ToyatoCar("Innova",'diesel')

# print(car1.name)
# print(car2.name)
# print(car1.start())

# Types of Inheritence
# 1 Single Inheritence : parent ---> child
# 2 Multi-level Inheritence : parent ---> child ---> child
# 3 Multiple Inheritence : parent1 + parent2 ---> child

# Super method
# super() method is used to access methods of the parent class
# print(car1.type)

# class method
# class Person:
#     name='anonymous'

    # def change_name(self,name):
    #     self.name=name

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=Person()
# p1.change_name("Aayush")
# print(p1.name) #Aayush
# print(Person.name) #anonymous
# p1.changeName("Aayush")
# print(Person.name) #Aayush

# property method
class Student:
    def __init__(self,phy,che,mat):
        self.phy=phy
        self.che=che
        self.mat=mat
        self.perc=str((phy+che+mat)/3)+"%"

    @property
    def percentage(self):
        perc=str((self.phy+self.che+self.mat)/3)+"%"
        print(perc)

stu=Student(98,97,96)
# print(stu.perc) #97%

stu.phy=95
# print(stu.perc) #97%
# print(stu.percentage) #96%  with the help of @property

# Poplymorphism
# when the same operator is allowed to have different meaning according to the context
# implicit overloading
# + operator have different role
# print(1+2) #3
# print("Aayush"+"patel") #Aayushpatel
# print([1,2,3]+[4,5,6]) #[1,2,3,4,5,6]

