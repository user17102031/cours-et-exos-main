👉 Cet algorithme glouton nécessite de commencer par les plus grandes puissances de 2 utiles.  
Dans la solution proposée, nous avons créé une liste des puissances de 2 triées par ordre croissant que nous avons parcourue à partir de la fin.

👉 Autre possibilité en utilisant `pop`

```python
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
    while len(puissances_utiles) > 0:
        p = puissances_utiles.pop()
        if p <= nombre:
            resultat = resultat + "1"
            nombre = nombre - p
        else:
            resultat = resultat + "0"

    return resultat
```

👉 Contrairement à ce que nous avons fait dans l'algorithme glouton de rendu de monnaie, il n'est pas nécessaire de constituer la liste des puissances de 2 utiles équivalente à la liste des pièces du rendu de monnaie. En effet, on trouve la puissance de 2 suivante à utiliser, par simple division entière par 2.

Autre solution possible, qui économise la création d'une liste :

```python
def binaire(nombre):
    if nombre == 0:
        return "0"
    resultat = ""

    puissance = 1
    while puissance <= nombre :
        puissance_max = puissance
        puissance = 2*puissance

    while puissance_max > 0:
        if nombre >= puissance_max:
            resultat = resultat + "1"
            nombre = nombre - puissance_max
        else:
            resultat = resultat + "0"
        puissance_max = puissance_max // 2

    return resultat
```


Visualisation du principe du binaire : [Cartes binaires](https://www.csfieldguide.org.nz/en/interactives/binary-cards/){ .md-button target="_blank" rel="noopener" }

