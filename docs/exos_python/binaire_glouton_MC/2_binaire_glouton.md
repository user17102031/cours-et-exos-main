---
author: Mireille Coilhac
title: Conversion gloutonne MC
tags:
  - 4-glouton
  - Difficulté ***
---

Pour convertir en base $2$ un entier écrit en base $10$, nous pouvons utiliser l'algorithme glouton de rendu de monnaie, en utilisant les puissances de $2$ successives comme valeurs des pièces.

Par exemple, pour obtenir la représentation binaire de $43$, on peut utiliser les valeurs $32$, $16$, $8$, $4$, $2$ et $1$. On se limite à $32$ car la puissance suivante, $64$, est strictement supérieure à $43$.

On procède alors ainsi :

* Pour $43$ on **peut** prendre $32$ , il reste $11$,
* Pour $11$ on **ne peut pas** prendre $16$ (en effet $16>11$),
* Pour $11$ on **peut** prendre $8$, il reste $3$,
* Pour $3$ on **ne peut pas** prendre $4$,
* Pour $3$ on **peut** prendre $2$, il reste $1$,
* Pour $1$ on **peut** prendre $1$, il reste $0$.

On obtient la représentation binaire en observant les différentes étapes : s'il est possible de prendre une puissance, on note un `#!py 1`, si c'est impossible, on note un `#!py 0`.

| Puissance de 2 | Possible ? | Bit correspondant |
| :------------: | :--------: | :---------------: |
|$32$| Oui | `#!py 1` |
|$16$| Non | `#!py 0` |
|$8$| Oui | `#!py 1`|
|$4$ | Non | `#!py 0`|
|$2$ | Oui | `#!py 1`|
|$1$ | Oui | `#!py 1`|

Dans la pratique, pour convertir « à la main » $43$ en binaire, cela revient réaliser le tableau suivant :

|$32$|$16$|$8$|$4$|$2$|$1$|
|:--:|:--:|:--:|:--:|:--:|:--:|
|`#!py 1`|`#!py 0`|`#!py 1`|`#!py 0`|`#!py 1`|`#!py 1`|


On en déduit que $43$ en décimal s'écrit `#!py 101011` en binaire.

???+ question "Travail à faire"

    Vous devez écrire une fonction `binaire` qui prend en paramètre un entier écrit en base $10$, et renvoie la chaîne de caractères la plus courte possible (sans zéros inutiles) représentant sa conversion en binaire.

!!! example "Exemples"

    ```pycon
    >>> binaire(43)
	'101011'
	>>> binaire(32)
	'100000'
	>>> binaire(0)
	'0'
	>>> binaire(54321)
	'1101010000110001'
	```

!!! danger "Contraintes"

    Vous utiliserez obligatoirement un algorithme glouton qui met en oeuvre la méthode décrite dans cet exercice.   
	L'utilisation de la fonction `bin` et du modulo (`%`) est interdite.

???+ question "Compléter le script ci-dessous"

    {{IDE('scripts/conversion_gloutonne', SANS = "bin")}}
