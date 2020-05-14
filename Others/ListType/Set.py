thisset = {"apple", "banana", "cherry"}
print(thisset)

print("\n")
for x in thisset :
    print("\t" + x)


print("\n")
print("banana" in thisset)

print("\n")
thisset.add("orange")
print(thisset)

print("\n")
thisset.update(["orange", "mango", "grapes"])
print(thisset)

print("\n")
print(len(thisset))

print("\n")
thisset.remove("banana")
print(thisset)

print("\n")
thisset.discard("apple")
print(thisset)

print("\n")
thisset.pop()
print(thisset)
print("\n")

print("\n")
del thisset
# print(thisset)
print("\n")

#Set operation

A = {1,2,3,5,6,7}
B = {5,7,8,9}
C = A.union(B)
print("A = "+format(A))
print("B = "+format(B))
print("A U B = "+format(C))

print("\n")
C = A.intersection(B)
print("A = "+format(A))
print("B = "+format(B))
print("A ^ B = "+format(C))

print("\n")
C = A.difference(B)
print("A = "+format(A))
print("B = "+format(B))
print("A - B = "+format(C))

print("\n")

























#Set operation Complited