u = input(("Skriv inn koordinatene til vektoren u = [x1, y1]: ")).split(",")
v = input(("Skriv inn koordinatene til vektoren v = [x2, y2]: ")).split(",")

skalarprodukt = float(u[0]) * float(v[0]) + float(u[1]) * float(v[1])

if skalarprodukt == 0:
    print("Vektorene er ortogonale.")
elif float(u[1]) * float(v[0]) == float(u[0]) * float(v[1]):
    print("Vektorene er parallelle.")
else:
    print("Vektorene er verken parallelle eller ortogonale.")
