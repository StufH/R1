from pylab import * #Importere pylab biblioteket for å bruke plotting
h = 1E-8 #Definere h for senere bruk i funksjonene

def f(x): #Her definerer du f(x)
    return x**2 + 2*x

def derivere(x):
    fder = (f(x + h) - f(x - h)) / (2*h) #Her er newtons symetriske kvotient
    return fder

x = linspace(-5, 5, 100) #Lager en array med punktene -5 til og med 5 med 100 punkter. Dette skal bli x verdiene
y = f(x) #her setter du y verdiene
der = derivere(x) #Her er y verdiene for den deriverte

plot(x, y) #Her plotter vi f(x)
plot(x, der) #Her plotter vi f'(x)
legend(["f(x)", "f'(x)"]) #Her navngir jeg de forskjellige grafene
axhline(y = 0, color = "black") #Her lager jeg to linjer i x = 0 og y = 0
axvline(x = 0, color = "black")
grid() #Her lager jeg en grid for å bedre se hvor grafene krysser
show() #Her viser jeg grafene