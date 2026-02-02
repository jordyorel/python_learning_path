"""
EXERCISE: 003
TITLE: Opérations mathématiques
DIFFICULTY: 1
CONCEPTS: arithmetic, operators
---
Python supporte les opérations mathématiques de base :

    addition       : 5 + 3   → 8
    soustraction   : 10 - 4  → 6
    multiplication : 3 * 4   → 12
    division       : 15 / 3  → 5.0
    puissance      : 2 ** 3  → 8

Calcule le résultat de chaque opération.
---
HINT: L'addition utilise le symbole +
HINT: La multiplication utilise * (pas x)
HINT: La puissance utilise ** (deux étoiles)
HINT: Respecte l'ordre : addition = 10 + 5, soustraction = 20 - 7, etc.
"""

# Calcule ces opérations
addition = ???       # 10 + 5
soustraction = ???    # 20 - 7
multiplication = ???  # 6 * 4
puissance = ???       # 3 ** 2

# Tests
assert addition == 15, f"addition devrait être 15, pas {addition}"
assert soustraction == 13, f"soustraction devrait être 13, pas {soustraction}"
assert multiplication == 24, f"multiplication devrait être 24, pas {multiplication}"
assert puissance == 9, f"puissance devrait être 9, pas {puissance}"

print(f"✓ Toutes les opérations sont correctes !")
print(f"  10 + 5 = {addition}")
print(f"  20 - 7 = {soustraction}")
print(f"  6 × 4 = {multiplication}")
print(f"  3² = {puissance}")