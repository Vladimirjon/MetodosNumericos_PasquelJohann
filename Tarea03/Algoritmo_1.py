def suma(n, x):
    sumatoria = 0
    for i in range(n):
        sumatoria += x[i]
    return sumatoria

valores = [3, 5, 7, 10]  
n = len(valores)
resultado = suma(n, valores)
print("La suma es:", resultado)