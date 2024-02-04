def et_logique(a, b):
    reponse = 0
    if a == 1:
        if b == 1:
            reponse = 1
    return reponse

# Tests
assert et_logique(0, 0) == 0
assert et_logique(0, 1) == 0
assert et_logique(1, 1) == 1
assert et_logique(1, 0) == 0
