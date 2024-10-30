def algoritmo2(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range (1,n-i):
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
                swapped = True
        if not swapped:
            break

ejemplo = [8,6,4,3,6,9]
algoritmo2(ejemplo)
ejemplo