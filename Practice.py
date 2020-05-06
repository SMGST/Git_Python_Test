import random
for x in range(10):
	print(random.randrange(1,100))
print()
for x in range(10, 20):
	print(x)
print()
for x in range(10, 101,10):
	print(x)
print()
a = "String"
for i in a:
	print(i)

print()
array = [10, 20, 30, 40, 50, 60]
for i in array:
	print(i)
b = "Hello, World!"
print(b[2:8])

b = "Hello, World!"
print(b[-6:-1])

a = " Hello, World! "
print(len(a))
a = a.strip()
print(a)
print(len(a))
print(a.lower())
print(a.upper())
print(a)
print(a.replace("He","Ja"))
a = a.split(",")
a[1] = a[1].strip()
print(a)

text = "The rain in Spain stays mainly in the plain"
print(text)
x = "ain" in text
print(x)
x = "ain" not in text
print(x)

print(a[0])
print(a[1])

b =  " " + a[1]
a = a[0]

c = a + b
print(c)

age = 21
text = "My Name is Tamim , I am " + format(age)
print(text)

quantity = 3
itemno = 567
price = 49.95
text = "I want {} pieces of item {} for {} dollars"
print(text.format(quantity,itemno,price))

classs = 4
age = 8
ball = 3
text = "I am Tashrif . I read in {1} . I have {2} Ball . I am {0} "
print(text)
text = text.format(age,classs,ball)
print(text)

text = "We are so Called \"Vikings\" From The North"
print(text)

singleQuote = "\'Single Quote\'"
print(singleQuote)
Backslash = "Backslash : \\"
print(Backslash)
CarriageReturn = "Carriage Return : \r"
print(CarriageReturn)
Octalvalue = "\110\145\154\154\157"
print(Octalvalue)
hex = "\x48\x65\x6c\x6c\x6f"
print(hex)

print("\n\n")
text = "Tamim"
text = text.casefold()
print(text)
text = text.capitalize()
print(text)
text = text.center(30) +"|"
print(text)
print(text.count("m"))
print(text.encode())
print(text.endswith("|"))	
print(text.endswith("a"))
print(text)
print(text)
print(text)
print(text)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
x = " ".join(myTuple)
print(x)
