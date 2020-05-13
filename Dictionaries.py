dic = {
    "খাবার" : "Food",
    "হাত" : "Hand",
    "পা" : "Leg",
    "চেহারা" : "Face",
    "কুত্তা" : "Dog",
    "বিলাই" : "Cat",
    "গরু" : "Cow",
    "year": 1964
}
print("------------------------------")
print(dic)
dic["year"] = "2020"
print(dic)
print("------------------------------\nx + \" \" + dic[x]")
for x in dic:
    print(x + " : " + dic[x])


print("------------------------------\nx in items method.")
for x in dic.items():
    print(x)
print("------------------------------\nx in Values method.")
for x in dic.values():
    print(x)

print("------------------------------\nx,y in items method.")
for x, y in dic.items():
    print(x, y)
print("------------------------------\nnew items added.")
dic["page"] = "20"
print(dic)
print("------------------------------\nitems removed.")
dic.pop("খাবার");
print(dic)

print("------------------------------")
while True:
    print(dic.get(str(input("Enter Word : "))))