import random

def randomArray(lb, ub, d):
    a = []
    for i in range(lb, ub):
        a.append(i)

    r = []
    for index in range(d):
        r.append(random.choice(a))
    return r

def extractRandomNumber(lb, ub):
    a = []
    for i in range(lb, ub):
        a.append(i)
    return random.choice(a)

#github demmerda porcooid

