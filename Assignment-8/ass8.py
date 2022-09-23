# Write a python script to compare two tuples, whether they contains the same elements in
# any order or not.
test_tup1 = (10, 4, 5)
test_tup2 = (13, 5, 18)

print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
res = all(x < y for x, y in zip(test_tup1, test_tup2))
print("Are all elements in second tuple greater than first ? : " + str(res))
