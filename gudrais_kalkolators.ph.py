print("Gudrais kalkolators")

darbiba = input("Ludzu ievasiet velamo darbibu(+ - * /): ")
a = int(input("Ludzu ievadi pirmo skaitli: "))
b = int(input("Ludzu ievadi otro skaitli: "))


if darbiba == "+":
    rez = a+b
elif darbiba == "-":
    rez = a-b
elif darbiba == "*":
    rez= a*b
elif darbiba == "/":
    rez = a/b
else:
    print("Sada darbiba nav atpazita")

print("Rezultats {} {} {} = {}".format(a, darbiba, b, rez))