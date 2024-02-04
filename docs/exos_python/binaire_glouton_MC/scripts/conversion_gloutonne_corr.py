def binaire(nombre):
    if nombre == 0:
        return "0"

    puissances_utiles = []
    p = 1
    while p <= nombre :
        puissances_utiles.append(p)
        p = 2 * p
    puissance_max = len(puissances_utiles) - 1
        
    resultat = ""          
    for i in range(puissance_max, -1, -1):
        puissance = puissances_utiles[i]
        if nombre >= puissance:
            resultat = resultat + "1"
            nombre = nombre - puissance
        else:
            resultat = resultat + "0"
    return resultat

