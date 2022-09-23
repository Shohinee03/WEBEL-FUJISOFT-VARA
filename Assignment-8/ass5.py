# Write a python script to count elements in a tuple.
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]
x = [j for i in enumerate(test_list) for j in i]
print(test_list)
print(len(x))
