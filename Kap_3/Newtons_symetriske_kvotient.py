def f(x):
    return x*2

def derivere(x, h):
    fder = (f(x + h) - f(x - h)) / (2*h)
    return fder

print(derivere(-1, 1E-8))