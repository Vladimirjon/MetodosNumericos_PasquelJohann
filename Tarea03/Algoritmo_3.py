def iterativo(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        i = 1
        while i <= n - 1:
            z = x + y
            x = y
            y = z
            i += 1
        return y

n = int(input("Introduce un número entero no negativo: "))
resultado = iterativo(n)
print("El número de Fibonacci es:", resultado)
