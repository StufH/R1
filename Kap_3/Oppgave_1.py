import numpy as np

intervall = input("skriv inn intervallet for eksempel (-1,2): ").split(",")
x1 = float(intervall[0])
x2 = float(intervall[1])

def f(x):
    return (x**2) * (np.e**x)

def snittfart():
    return (f(x2) - f(x1)) / (x2 - x1)


snitt = round(snittfart(), 4)
print(f"gjennomsnittlig vekstfart i intervallet [{x1}, {x2}] er {snitt}")

fil = open("vekstfart.txt", "a")
fil.write(f"gjennomsnittlig vekstfart i intervallet [{x1}, {x2}] er {snitt}\n")
fil.close()