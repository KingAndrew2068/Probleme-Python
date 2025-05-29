def este_palindrom(cuvant):
    return cuvant == cuvant[::-1]

cuvant = input("Introduceti un cuvant: ")

if este_palindrom(cuvant):
    print(f"{cuvant} este un palindrom!")
else:
    print(f"{cuvant} nu este un palindrom.")
