print("----------------------------------------------------------------------------")
class MyClass:
    x = 5

class Student:
    def __init__(thisIns,roll,name):
        # First parameter  of any function inside class is a reference to the current instance of the class
        # Can be Named anything Considering Naming Convention
        thisIns.roll = roll
        thisIns.name = name

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def details(self):
        print('********** "Details" Function of "Person" class **********\n')
        print("Hello , my name is " + self.name)
        print("I am " + self.age +" years old now.")


print(MyClass)
obj = MyClass()
print(obj.x)

p1 = Student(2,"Tamim")
print(p1.roll)
print(p1.name)

per = Person("Tashrif","8")
per.details()
print('Two Years Letter')
per.age = '10'
per.details()