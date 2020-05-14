class Person:
  def __init__(self, fname, lname):
    print('********** "Constructor" of "Person" class **********\n')
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    pass


class Man():
    def __init__(self, fname, lname):
        print('********** "Constructor" of "Man" class **********\n')
        self.firstname = fname
        self.lastname = lname
class Woman():
    def __init__(self, fname, lname):
        print('********** "Constructor" of "Woman" class **********\n')
        self.firstname = fname
        self.lastname = lname

class Sir(Person,Man):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print('********** "Constructor" of "Sir" class **********\n')
        print('********** "Inheriting (Person,Man) **********\n')
class Madam(Woman, Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print('********** "Constructor" of "Madam" class **********\n')
        print('********** "Inheriting (Women,Person) **********\n')


x = Student("John", "Doe")
x.printname()

s = Sir('Tamim','Sarker')
print('----------------------------------------------------')
mam = Madam('Feminist','Women')