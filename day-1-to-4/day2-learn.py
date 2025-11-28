

# First-class Functions in Python
    # - A function can be stored in a variable or value
    # - A parameter of a function can be a function
    # - The return value of a function can be a function
    

def greet():
    print("Hello")
hello = greet  # Function as value

# HOF: Higher Order Function
# why use HOF?
# 1. Code Reusability
# 2. Separation of Concerns
# 3. Decorators
def with_emoji(func,emoji="😊"):  # Function as parameter
    def wrapper():
        print(emoji, end=" \n")
        func()
        print(emoji)
    return wrapper # Function as return value

# greet()  # Calling the original function
# hello()  # Calling the function stored in a variable
# hello_with_emoji = with_emoji(hello, "🙋‍♂️")  # Wrapping the greet function
# hello_with_emoji()  # Calling the wrapped function



# Example 2


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Requirement-1: Get all even numbers from the list
def filter_even(nums):
    even_nums = []
    for n in nums:
        if n % 2 == 0:
            even_nums.append(n)
    return even_nums

even_numbers = filter_even(numbers)
print("Even Numbers:", even_numbers)

# Requirement-2: Get all odd numbers from the list
def filter_odd(nums):
    odd_nums = []
    for n in nums:
        if n % 2 != 0:
            odd_nums.append(n)
    return odd_nums

odd_numbers = filter_odd(numbers)
print("Odd Numbers:", odd_numbers)

# Requirement-3: Get all numbers greater than 5 from the list
def filter_greater_than_five(nums):
    greater_nums = []
    for n in nums:
        if n > 5:
            greater_nums.append(n)
    return greater_nums

greater_than_five_numbers = filter_greater_than_five(numbers)
print("Numbers Greater than 5:", greater_than_five_numbers)


# code-style : imperative programming
# -> intention + implementation mixed together
# solution: declarative programming

def filter_numbers(nums, condition_func):  # HOF
    filtered_nums = []
    for n in nums:
        if condition_func(n):
            filtered_nums.append(n)
    return filtered_nums

# Condition functions
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def is_greater_than_five(n):
    return n > 5

even_numbers = filter_numbers(numbers, is_even)
print("Even Numbers (HOF):", even_numbers)

odd_numbers = filter_numbers(numbers, is_odd)
print("Odd Numbers (HOF):", odd_numbers)

greater_than_five_numbers = filter_numbers(numbers, is_greater_than_five)
print("Numbers Greater than 5 (HOF):", greater_than_five_numbers)

# Lambda Functions
even_numbers_lambda = filter_numbers(numbers, lambda n: n % 2 == 0)