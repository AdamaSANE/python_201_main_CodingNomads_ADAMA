# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(sequence, start=0):
      """
      Custom implementation of Python's built-in enumerate().
      Yields pairs of (index, value) from the given sequence, starting from 'start'.
      """
      idx = start  # Initialize the index
      for item in sequence:
            yield idx, item  # Yield a tuple (index, item)
            idx += 1  # Increment the index for the next item

# Example usage
courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']
# Use my_enumerate as a drop-in replacement for enumerate
for index, course in my_enumerate(courses):
      print(f"{index}: {course} Python")

# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python
