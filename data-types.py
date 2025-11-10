
# Data Types in Python

# ------------------------------------------------------------
# 1. Simple/Primitive Data Types ( holding single values )
# ------------------------------------------------------------

#a.Numeric Types - int, float, complex
int_variable = 42
float_variable = 3.14
complex_variable = 1 + 2j
print(f"Integer Type: {int_variable} (Type: {type(int_variable)})")
print(f"Float Type: {float_variable} (Type: {type(float_variable)})")
print(f"Complex Type: {complex_variable} (Type: {type(complex_variable)})")

#b.Boolean Type - bool
bool_variable = True
print(f"Boolean Type: {bool_variable} (Type: {type(bool_variable)})")

#c.Text Type - str
text_variable = "Hello, World!"
print(f"Text Type: {text_variable} (Type: {type(text_variable)})")

#d.None Type - NoneType. ( similar to null in other languages )
none_variable = None
print(f"None Type: {none_variable} (Type: {type(none_variable)})")

# ------------------------------------------------------------
# 2.Complex/Collection Data Types ( holding multiple values )
# ------------------------------------------------------------

# a.sequence types: list, tuple, range ( holding ordered values , indexed , allowing duplicates )

# List
fruits = ["apple", "banana"]
print(f"List: {fruits} (Type: {type(fruits)})")
# Tuple
coordinates = (10, 20)
print(f"Tuple: {coordinates} (Type: {type(coordinates)})")

# List vs Tuple
# Lists are mutable (can be changed), tuples are immutable (cannot be changed)
fruits[0] = "orange"  # Modifying list
print(f"Modified List: {fruits}")
# coordinates[0] = 15  # This would raise an error

# Range
number_range = range(1, 10)
print(f"Range: {number_range} (Type: {type(number_range)})")


# b. set types: set, frozenset ( holding unordered values , unindexed , no duplicates )
# Set
unique_numbers = {1, 2, 3, 4, 5, 5 }  # Duplicates are ignored
print(f"Set: {unique_numbers} (Type: {type(unique_numbers)})")
# Frozenset
immutable_set = frozenset([1, 2, 3, 4, 5, 5])  # Duplicates are ignored
print(f"Frozenset: {immutable_set} (Type: {type(immutable_set)})")

# set vs frozenset
# Sets are mutable, frozensets are immutable
unique_numbers.add(6)  # Modifying set
print(f"Modified Set: {unique_numbers}")
# immutable_set.add(6)  # This would raise an error

# c. mapping type: dict ( holding key-value pairs , unordered , indexed by keys )
# Dictionary
person = {"name": "Alice", "age": 30}
print(f"Dictionary: {person} (Type: {type(person)})")

# --------------------------------------------------------------
# custom data types can also be created using classes
# --------------------------------------------------------------

# Bank - account example
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
# Creating an instance of Account
my_account = Account("123456789", 1000)
# display account and type
print(f"Account Number: {my_account.account_number}, Balance: {my_account.balance} (Type: {type(my_account)})")



# ---------------------------------------------------------------

x=12
print(f"x: {x} (Type: {type(x)})")
x="hello"
print(f"x: {x} (Type: {type(x)})")

# ---------------------------------------------------------------