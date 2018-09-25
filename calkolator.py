print("Kalkulators 1.0")

x = input("Ludzu ievadiet X: ")
y = input("Ludzu ievadiet Y: ")

rez = int(x) + int(y)
print("Rezultats: ", x," + ", y," = ", rez)
if rez > 50:
    print("Rezultats ir lielaks par 50")
elif rez == 50:
print("Rezultats ir 50")
else:
    print("Rezultats ir mazalks par 50")