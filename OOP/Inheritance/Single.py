class A:
    def feature1(self):
        print("This is feature A1")
    def feature2(self):
        print("This is feature A2")
class B(A):
    def feature3(self):
        print("This is feature B3")
    def feature4(self):
        print("This is feature B4")

obj = A()
obj.feature1()
obj.feature2()
print()

a1 = B()
a1.feature1()
a1.feature2()
a1.feature3()
a1.feature4()