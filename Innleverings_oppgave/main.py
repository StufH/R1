from pylab import *
import numpy as np
from scipy.optimize import curve_fit

vinkel = []
akselerasjon = []

# Åpne fil
fil = open("R1_matte_eskperiment_prog.csv", "r")
fil.readline()
# Lese av fil
for rad in fil:
    data = rad.split(",")
    vinkel.append(float(data[0]))
    akselerasjon.append(float(data[1]))
fil.close()

gjetning = [9.0, 1.0, 0.0, 0.0]

def sinus(x, A, phi, c, d):
    return A*np.sin(c*x + phi) + d

def f(x, a, b, c):
    return a*x**2 + b*x + c

params, _ = curve_fit(sinus, vinkel, akselerasjon, p0=gjetning, maxfev=5000)
a1, b1, c1 = polyfit(vinkel, akselerasjon, deg=2)

x = (linspace(0, 90, 100))
y1 = sinus(x, params[0], params[1], params[2], params[3])
y2 = f(x, a1, b1, c1)

plot(x, y1, color="purple")
plot(x, y2, color="green")
plot(vinkel, akselerasjon, ".", color="blue")
legend(["sinus", "andregrads"])
xlabel("vinkel")
ylabel("akselerasjon")
grid()
show()

# bruk halverings metoden for å finne toppunkt til grafen for å se om det er 9.81

#
# d = (max(akselerasjon) + min(akselerasjon)) / 2
# A = (max(akselerasjon) - min(akselerasjon)) / 2
# def c(x):
#     return (2*pi)/x
#
# def phi(phi, c):
#     return -((phi)/c)