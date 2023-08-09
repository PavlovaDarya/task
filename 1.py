from random import randint

def f1():
    l=[]
    while len(l) < 100:
        x=randint(1,1000001)
        if x not in l:
            l.append(x)
    return l
print (f1())
