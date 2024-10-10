n = 0
t = []

fil = open("Lagring-testing.txt", "w")

while (n < 10):
    n += 1
    fil.write(str(2**(2-n)) + ", ")
fil.close()

fil = open("Lagring-testing.txt", "r")
Data = fil.read()
file = Data.split()
fil.close()

file = " ".join(file)
print(file)
s = sum(file)
print(s.as_integer_ratio())