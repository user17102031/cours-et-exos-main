---
author: Mireille Coilhac
title: Couper un jeu de cartes MC
tags:
  - 3-liste/tableau
---

Couper un jeu de cartes consiste à prendre une partie des cartes depuis le dessus du paquet pour les passer sans en modifier l'ordre sous le paquet. Ceci permet d'éviter une triche lors de la distribution des cartes. De façon analogue, nous allons couper un tableau.

La fonction `coupe` prend en paramètres `tableau` qui est un tableau de taille supérieure ou égale à 2 et `nombre` qui est un entier représentant le nombre de cartes mises en dessous. La fonction `coupe` renvoie un nouveau tableau constitué des éléments de `tableau` pour lesquels les `nombre` premiers éléments ont été transférés dans cet ordre du début du tableau à la fin.

!!! warning "Limitations"

	On garantit que `tableau` est de longueur `n` supérieure ou égale à 2, et que `nombre` est un entier pouvant prendre toutes les valeurs de 1 à `n`- 1

!!! danger "Contrainte"

	L'utilisation des tranches ("slices" en anglais) est interdite.

!!! example "Exemple"

    ```pycon
    >>> coupe(['As ♠', '5 ♥', '2 ♠', '5 ♣', 'Dame ♠', '8 ♦', 'As ♣', 'Valet ♣'], 3)
	['5 ♣', 'Dame ♠', '8 ♦', 'As ♣', 'Valet ♣', 'As ♠', '5 ♥', '2 ♠']
    >>> coupe([5, 1, 8, 3, 7], 1)
	[1, 8, 3, 7, 5]
    >>> coupe([5, 1, 8, 3, 7], 2)
	[8, 3, 7, 5, 1]
	>>> coupe([5, 1, 8, 3, 7], 4)
	[7, 5, 1, 8, 3]
	>>> coupe([5, 3], 1)
	[3, 5]
	```

???+ question "Travail à faire"

    Vous devez écrire la fonction `coupe`.

    {{IDE('scripts/coupe_cartes')}}


