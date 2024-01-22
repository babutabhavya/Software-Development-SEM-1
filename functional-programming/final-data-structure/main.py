# Creating a tuple
my_tuple = (1, 2, 3, 4)

# Accessing elements of the tuple
print(my_tuple[0])

# Attempting to modify the tuple (will raise an error)
try:
    my_tuple[0] = 10
except (
    TypeError
) as e:  # Raises: TypeError: 'tuple' object does not support item assignment
    print(f"Error: {e}")

# Concatenating tuples to create a new tuple
new_tuple = my_tuple + (5, 6)
print(new_tuple)
