# h = 1E-8    #Variablene jeg blir å få bruk for i koden min
# b = 2
# a = 8
# z = 0
# zd = 0.00001
#
# def f(x):       #her definerer jeg funksjonen
#     return d*x**2 + g*x + n
#
# Augustin = (f(b) - f(a)) / (b - a)  #Her definerer jeg Augustin sin formel
#
# def derivere(x):    #Her bruker jeg newtons symmetriske kvotient for å finne den deriverte
#     fder = (f(x + h) - f(x - h)) / (2*h)
#     return fder
#
#
# while Augustin - derivere(z) >= zd: #Her finne jeg ut om verdien for den deriverte er lik i både Augustin sin forel og Newtons
#     if Augustin >= derivere(z):     #Her sjekker jeg om der er forskjellige fra positiv side eller negativ side
#         z += zd
#     elif Augustin < derivere(z):    #Her sjekker jeg om der er forskjellige fra positiv side eller negativ side
#         z -= zd
#
# print(f"Verdien for c = {round(z, 4)}") #Her printer jeg verdien etter at forskjellen mellom augustin sin formel og Newtons formel er lik nok
#

h = 1E-8    #Variablene jeg blir å få bruk for i koden min
b = 2
a = 8
z = 0
zd = 0.00001
d = 1
g = 1
n = 1

for i in range(1000): #Her kjører jeg programmet flere ganger
    def f(x):
        return d*x**2 + g*x + n

    Augustin = (f(b) - f(a)) / (b - a)  

    def derivere(x):
        fder = (f(x + h) - f(x - h)) / (2*h)
        return fder


    while Augustin - derivere(z) >= zd: 
        if Augustin >= derivere(z):     
            z += zd
        elif Augustin < derivere(z):    
            z -= zd

    print(f"Verdien for c ved funksjonen {d}x^2 + {g}x + {n} = {round(z, 4)}")
    d += 1 #Her legger jeg til verdier for variablene jeg la til i funksjon så den endrer seg for hver loop
    g += 3
    n += 20

