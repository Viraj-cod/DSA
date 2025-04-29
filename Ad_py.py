####################################Ad PY #####################################
def add(f):
    def berij(a,b):
        if a > b:
            print(a*b)
        else:
            print(a+b)
        f(a,b)
        return 'decorator finished!'
    return berij

@add
def asach(e,w):
    print('In decorator')
print(asach(9,6))


k = lambda x:x**2 # lamda or anaonymous function
#print(k(66))
o=[2,3,4,5,6]
def oi(l):
    if l % 2 == 0:
        return l
j=map(oi,o) # map function : map function applies the function to evry value in dataset  

print(list(j))
pi=filter(oi,o) # filter function: filters the dataset based of given function

print('filter',list(pi))
p=[i**3 for i in range(1,9) if i % 2 == 1] #list comprehension
#print(p)

from functools import reduce
m=[2,3,4,5]
op=lambda x,y:x+y

p=reduce(op,m)
print(p)

k=1
if k ==0:
    raise AttributeError("k should not be zero")
    
