# Write a python script to calculate average of tuple values. Assuming values are of int type
# # only.
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result
nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",
      average_tuple(nums))
