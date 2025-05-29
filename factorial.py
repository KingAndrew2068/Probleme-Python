def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

numar = int(input("Introduceti un numar pentru a calcula factorialul: "))
print(f"Factorialul lui {numar} este {factorial(numar)}.")
