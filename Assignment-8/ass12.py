# Write a python script to count the frequency of elements of a tuple.
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

print("The original tuple is : " + str(test_tup))
 
res = dict()
x=list(test_tup)
y=[]
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    res[i]=x.count(i)
# printing result
print("Tuple elements frequency is : " + str(res))
