from math import *
def Probability(sum, times) :
    favorable, total, probability = 0.0, 36.0, 0
    for i in range(7) :
        for j in range(7) :
            if ((i + j) == sum) :
                favorable += 1
 
    gcd1 = gcd(int(favorable), int(total))
    favorable = favorable / gcd1
    total = total / gcd1
    probability = pow(total, times)
 
    return int(probability)
if __name__ == "__main__" :
    sum, times = 7, 7
    print("1","/",Probability(sum, times))
