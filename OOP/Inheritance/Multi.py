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
class C(B):
    def feature5(self):
        print("This is feature C5")
    def feature6(self):
        print("This is feature C6")


obj = A()
obj.feature1()
obj.feature2()
print()

obj2 = B()
obj2.feature1()
obj2.feature2()
obj2.feature3()
obj2.feature4()
print()

a1 = C()
a1.feature1()
a1.feature2()
a1.feature3()
a1.feature4()
a1.feature5()
a1.feature6()