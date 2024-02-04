# Tests
assert coupe(['As ♠', '5 ♥', '2 ♠', '5 ♣', 'Dame ♠', '8 ♦', 'As ♣', 'Valet ♣'], 3) == ['5 ♣', 'Dame ♠', '8 ♦', 'As ♣', 'Valet ♣', 'As ♠', '5 ♥', '2 ♠']
assert coupe([5, 1, 8, 3, 7], 1) == [1, 8, 3, 7, 5]
assert coupe([5, 1, 8, 3, 7], 2) == [8, 3, 7, 5, 1]
assert coupe([5, 1, 8, 3, 7], 4) == [7, 5, 1, 8, 3]
assert coupe([5, 3], 1) == [3, 5]

# Autres tests
from random import randint
nombre = randint(0, 99)
nombres = [randint(1, 2**10) for _ in range(100)]
attendu = nombres[nombre:] + nombres[:nombre]
assert coupe(nombres, nombre ) == attendu
