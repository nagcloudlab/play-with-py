
# data-structures With Iterator -> Iterable

iterable=[1, 2, 3, 4, 5]

# map
func = lambda x: x**2
squared_iterable = map(func, iterable)
list_squared = list(squared_iterable)
print(list_squared)  # Output: [1, 4, 9, 16

# filter
filter_func = lambda x: x % 2 == 0
filtered_iterable = filter(filter_func, iterable)
list_filtered = list(filtered_iterable)
print(list_filtered)  # Output: [2, 4]

# zip
iterable2 = ['a', 'b', 'c', 'd', 'e']

zipped_iterable = zip(iterable, iterable2)
list_zipped = list(zipped_iterable)
print(list_zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# reduce
from functools import reduce
reduce_func = lambda x, y: x + y
reduced_value = reduce(reduce_func, iterable) 
# x=1, y=2 -> 3
# x=3, y=3 -> 6
# x=6, y=4 -> 10
# x=10, y=5 -> 15
print(reduced_value)  # Output: 15

