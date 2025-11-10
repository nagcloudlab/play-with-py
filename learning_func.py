

# what is function ?
# A function is a block of reusable code that performs a specific task.

# how to define a function in python ?

# function with no arguments and no return value
def greet1():
    print("Hello, World!")
    print("😀")

greet1()  # Calling the function
# Output: Hello, World!
greet1()  # Calling the function again
# Output: Hello, World!

# function with arguments and no return value
def greet2(name):
    print(f"Hello, {name}!")
    print("😀")
greet2("Alice")  # Calling the function with an argument
# Output: Hello, Alice!
greet2("Bob")    # Calling the function with another argument
# Output: Hello, Bob!

# function with arguments and return value
def add(a, b):
    result = a + b
    return result

sum1 = add(3, 5)  # Calling the function and storing the return value
print(sum1)  # Output: 8
sum2 = add(10, 20)  # Calling the function with different arguments
print(sum2)  # Output: 30


# function with default arguments
def greet3(name="Guest"):
    print(f"Hello, {name}!")
    print("😀")
greet3()  # Calling the function without an argument
# Output: Hello, Guest!
greet3("Charlie")  # Calling the function with an argument
# Output: Hello, Charlie!

# function with variable number of arguments ( varargs | rest parameters )
def greet4(*names):
    # type of names is tuple
    print(f"Type of names: {type(names)}")

greet4()  # Calling the function with no arguments
# Output: Type of names: <class 'tuple'>
greet4("Dave")  # Calling the function with one argument
# Output: Type of names: <class 'tuple'>
greet4("Eve", "Frank")  # Calling the function with multiple arguments
# Output: Type of names: <class 'tuple'>


# function with keyword arguments
def greet5(**kwargs):
    # type of kwargs is dict
    print(f"Type of kwargs: {type(kwargs)}")
greet5()  # Calling the function with no arguments
# Output: Type of kwargs: <class 'dict'>
greet5(name="Grace")  # Calling the function with one keyword argument
# Output: Type of kwargs: <class 'dict'>
greet5(name="Heidi", age=30)  # Calling the function with multiple keyword arguments
# Output: Type of kwargs: <class 'dict'>
# function with both positional and keyword arguments
greet5(age=25, name="Ivan", address="Universe")  # Calling the function with both types of arguments
# Output: Type of kwargs: <class 'dict'>

