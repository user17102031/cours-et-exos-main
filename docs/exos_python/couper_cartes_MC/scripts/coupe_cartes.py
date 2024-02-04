def coupe(tableau, nombre):
    ...


# Tests
paquet_1 = ['As ♠', '5 ♥', '2 ♠', '5 ♣', 'Dame ♠', '8 ♦', 'As ♣', 'Valet ♣']
paquet_2 = ['5 ♣', 'Dame ♠', '8 ♦', 'As ♣', 'Valet ♣', 'As ♠', '5 ♥', '2 ♠']
assert coupe(paquet_1, 3) == paquet_2
assert coupe([5, 1, 8, 3, 7], 1) == [1, 8, 3, 7, 5]
assert coupe([5, 1, 8, 3, 7], 2) == [8, 3, 7, 5, 1]
assert coupe([5, 1, 8, 3, 7], 4) == [7, 5, 1, 8, 3]
assert coupe([5, 3], 1) == [3, 5]


