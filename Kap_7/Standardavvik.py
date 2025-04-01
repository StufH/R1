from pylab import *

# Data:
y = array([3.73, 3.53, 3.75, 3.63, 3.82])
n = len(y)

# Beregning av snitt og standardavvik:
y_snitt = sum(y) / n
s = sqrt(sum((y - y_snitt)**2) / (n-1))

# beregning av standardfeil:
se = s / sqrt(n)

print(f"gjennomsnittet er: {round(y_snitt, 3)}")
print(f"standardavviket er: {round(s, 3)}")
print(f"standardfeilen er: {round(se, 3)}")

#plotting av data:
plot(y,y_snitt, "b.")
vlines(y, y_snitt - 2 * se, y_snitt + 2 * se, "r")
xlabel("Måling")
ylabel("Verdi")
title("Standardavvik")
show()