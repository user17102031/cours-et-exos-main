# Tests

assert binaire(43) == '101011'
assert binaire(32) == '100000'
assert binaire(0) == '0'
assert binaire(54321) == '1101010000110001'


# Autres tests

assert binaire(10922) == '10101010101010'
assert binaire(32319) == '111111000111111'
assert binaire(4095) == '111111111111'
for n in range(2**5, 2**10):
    attendu = bin(n)[2:]
    assert binaire(n) == attendu, f"Erreur avec la conversion de {n}"

