def f(x):
    return x**3 + 2*x - 7

def derivere(x, h):
    fder = (f(x + h) - f(x - h)) / (2*h)
    return fder

print(derivere(2, 1E-15))