def suma_cifrelor(numar):
    suma = 0
    while numar > 0:
        suma += numar % 10
        numar //= 10
    return suma

numar = int(input("Introduceti un numar: "))

if numar % 2 == 0 and numar % 3 == 0 and suma_cifrelor(numar) > 10:
    print(f"{numar} este un numar misterios!")
else:
    print(f"{numar} nu este un numar misterios.")
