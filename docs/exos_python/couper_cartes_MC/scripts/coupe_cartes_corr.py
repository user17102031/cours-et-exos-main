def coupe(tableau, nombre):
    n = len(tableau)
    nouveau = [None] * n
    for i in range(nombre):
        nouveau[n - nombre + i] = tableau[i]
    for i in range(nombre, n):
        nouveau[i - nombre] = tableau[i]
    return nouveau

    