from pylab import *

y = array([3.73, 3.53, 3.75, 3.63, 3.82])
n = len(y)
y_snitt = sum(y) / n
s = sqrt(sum((y - y_snitt)**2) / (n-1))

print(f"gjennomsnittet er: {y_snitt}")
print(f"standardavviket er: {s}")