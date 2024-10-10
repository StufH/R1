from pylab import *

k = 0.035
l = 0
x = 0

L = l*e**(-k*x)

l_pros = l*0.5

while L > l_pros:
    x =+ 1
    l =-1
    print(L)

if L == l_pros:
    print(L)
