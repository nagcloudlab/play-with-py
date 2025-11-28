


# Exception vs Error
# ---------------------

# Example of Exception: ZeroDivisionError, ValueError, TypeError

def divide(a, b):
    return a / b  # This can raise ZeroDivisionError if b is 0

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")


# Example of RecursionError

def recursive_function():
    return recursive_function()

try:
    recursive_function()
except RecursionError as e:
    print(f"Caught a recursion error: {e}")


try:
    import sys
    sys.exit()
except SyntaxError:
    print("Won't catch SystemExit")

print("End of the program.")