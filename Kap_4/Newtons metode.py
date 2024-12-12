from pylab import *
delta_x = 0.00001

def f(x):
    return x*log(x) - 1

x = linspace(delta_x, 7, 1000)
y = f(x)

plot(x, y, color = "b")
ylim(-20, 40)
axhline(y = 0, color = "k")
axvline(x = 0, color = "k")
xlabel("x")
ylabel("y")
grid()
show()

x1 = float(input("Skriv inn en x-verdi nær nullpunktet: "))



def f_derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

def ny_x_verdi(x1):
    return x1 - (f(x1) / f_derivert(x1))

for i in range(100):
    x2 = ny_x_verdi(x1)
    if abs(x1 - x2) > 0.0000001:
        print(f"Et bedre forslag er gitt ved x = {round(x2, 4)}")
        x1 = x2
    else:
        break

print(f"Med x = {x1} er f(x) = {f(x1)}")