list = ["Apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Hole list\n\t")
print(list)
print(list[1])
print(list[-1])
print(list[2:5])
print(list[2:])
print(list[:5])
print(list[-5:-1])
print(list[:-3])
print(list[-5:])








list[1] = "blackcurrant"
print(list)

for x in list:
    print(x)

if "apple" in list:
    print("Yes, 'apple' is in the fruits list")

print(len(list))

list.append("Blackbary")
print(list)

print("\n")
list.insert(1, "Tamim")
print(list)

print("\n")
list.pop()
print(list)

print("\n")
del list[1]
print(list)

print("\n")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)

print("\n")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print("\n")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

print("\n")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list1)
print(list2)
print(list3)

print("\n")
list1.extend(list2)
print(list1)

print("\n")


print("\n\n\n")
