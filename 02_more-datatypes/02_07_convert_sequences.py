# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tuple_from_string = tuple(string)
list_from_tuple = list(tuple_from_string)
list_from_tuple[0] = 'k'
final_tuple = tuple(list_from_tuple)
print(final_tuple)
