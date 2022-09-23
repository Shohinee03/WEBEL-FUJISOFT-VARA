# Write a python script to calculate sum of elements of the tuple. Tuple input is taken from
# keyboard (all values are of int type).

myTuple = ([7, 8], [9, 1, 10, 7])
print("The original tuple is : " + str(myTuple)) 
tupSum = sum(list(map(sum, list(myTuple)))) 
print("The summation of tuple elements are : " + str(tupSum))
