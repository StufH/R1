import math

a_list = []
b_list = []

def vector(a, b):
    return math.sqrt(a**2 + b**2)

def telle_vektorer(max_verdi):
    count = 0
    for a in range(-max_verdi, max_verdi + 1):
        for b in range(-max_verdi, max_verdi + 1):
            if vector(a, b) == max_verdi:
                count += 1
                a_list.append(a)
                b_list.append(b)

    return count

for i in range(0,100):
    max_verdi = i
    result = telle_vektorer(max_verdi)
    print(f"Antall vektorer med lengde {max_verdi} = {result}")
    print(f"a og b verdier: {list(zip(a_list, b_list))}")
    print("")
    a_list.clear()
    b_list.clear()

#max_verdi = int(input("Skriv inn en verdi for maksimal vektorlengde: "))