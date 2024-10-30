def serie_armonica(n):
    suma = 0
    for i in range(1, n + 1):
        suma += 1 / i
    return suma

n = int(input("Introduce el número de términos a sumar: "))
resultado = serie_armonica(n)
print(f"La suma de los primeros {n} términos es: {resultado}")