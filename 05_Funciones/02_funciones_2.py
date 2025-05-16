
# if we don't know how many parameters will have a function, we can use '*'
# to specify that we dont know how many parameters it will have.

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emma", "Simon", "Rafa", "Sophia")


print("--------------------------------")

# Here we are using 'keyword arguments' that are burned values.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


print("---------------------------------")

# In this function if we don't put a parameter, the function allocate "Norway" 
# by default. If we put something in the parameter, this one will be used
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


print("----------------------------------")


# Passing a List as an Argument.
# Here we are using a list as the function argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



print("----------------------------------")


# The pass Statement
# Here we are using the 'pass' statement to ignore the code inside of the function,
# and to continue with the next
def myfunction():
    pass



print("----------------------------------")


