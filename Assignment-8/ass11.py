# Write a python script to compare two tuples, whether they contains the same elements in
# same order or not.
my_tuple_1 = (87, 90, 31, 85)
my_tuple_2 = (34, 56, 12, 5)

print("The first tuple is :")
print(my_tuple_1)
print("The second tuple is :")
print(my_tuple_2)

my_result = set(my_tuple_2).issubset(my_tuple_1)

print("Is the second tuple a subset of the first tuple ? ")
print(my_result)
