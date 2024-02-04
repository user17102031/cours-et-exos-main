Autre correction possible en utilisant le "modulo": 

```python
def coupe(tableau, nombre):
    n = len(tableau)
    return [tableau[(i + nombre) % n] for i in range(n)]
```

On peut également utiliser les indices de listes négatifs : 

```python
def coupe(tableau, nombre):
    n = len(tableau)
    d = nombre - n
    return [tableau[d + i] for i in range(n)]
```



