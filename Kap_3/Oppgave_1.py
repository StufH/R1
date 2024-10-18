"""
def f(x):
    return 0.06*x**2 + 4*x - 7

def snittfart(f, x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)

snitt = round(snittfart(f, -1, 3), 2)
print(f"gjennomsnittlig vekstfart i intervallet [-1, 3] er {snitt}")
"""
intervall = input("skriv inn intervallet for eksempel (-1,2): ").split(",")
x1 = float(intervall[0])
x2 = float(intervall[1])

def g(x):
    return 2*x**3

def snittfart(g):
    return (g(x2) - g(x1)) / (x2 - x1)

snitt = round(snittfart(g), 2)
print(f"gjennomsnittlig vekstfart i intervallet [{x1}, {x2}] er {snitt}")