def my_Function():
    print("it is printing from function")

def function(fname):
    print("Hello ," + fname)

def unKnown_args(*ar):
    print("Secend Arguments : " + str(ar[1]))
    print("All Arguments : ")
    for x in ar:
        print(x)
def keyword(ar2,ar3,ar1):
    print("Argument no 1 = " + str(ar1))
def unknown_Keyword(**kid):
    print("His First name is " + kid["fname"])
    print("His last name is " + kid["lname"])

def defualt_Value(country = "Norway"):
    print("I am from " + country)

def print_List(list):
    for x in list:
        print(x)

def sum(a,b):
    return a+b
def myfunction():
    pass
# having an empty function definition like this, would raise an error without the pass statement
def tri_recursion(k):
    if(k<0):
        return 0
    result = k + tri_recursion(k-1)
    print(result)
    return result

# lambda function
x = lambda a:a*10
multipliction = lambda a,b:a*b

# lambda inside function
def funLambda(n):
    return lambda a:a-n


myfunction()
print("------------------------------")
my_Function()
print("------------------------------")
function("Tamim")
print("------------------------------")
unKnown_args(1,2,3)
unKnown_args("C","C++","java","Python")
print("------------------------------")
keyword(ar1="Laptop",ar2="Mobile",ar3="TV")
print("------------------------------")
unknown_Keyword(fname = "Tobias", lname = "Refsnes")
print("------------------------------")
defualt_Value("Sweden")
defualt_Value("India")
defualt_Value()
defualt_Value("Brazil")
print("------------------------------")
list = ["C","C++","java","Python"]
print_List(list)
print("------------------------------")
tuples = ("Name","Roll","Dep")
print_List(tuples)
print("------------------------------")
print(sum(5,4))
print("------------------------------")
print("Recursion Example Results")
tri_recursion(7)
print("------------------------------\n\n\t# Lambda function")
print(x(5))
print(multipliction(5,6))
print("------------------------------\n\n\t# lambda inside function")
print(funLambda(2)(7))
z = funLambda(3)
print(z(10))
print("------------------------------")
