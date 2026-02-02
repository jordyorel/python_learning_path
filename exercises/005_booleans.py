"""
EXERCISE: 005
TITLE: Booléens et comparaisons
DIFFICULTY: 2
CONCEPTS: boolean, comparison, operators
---
Les booléens sont des valeurs True (vrai) ou False (faux).

Opérateurs de comparaison :
    ==  égal à
    !=  différent de
    >   supérieur à
    <   inférieur à
    >=  supérieur ou égal
    <=  inférieur ou égal

Exemples :
    5 > 3      → True
    10 == 10   → True
    7 < 5      → False
    "chat" == "chien"  → False

Complète les comparaisons.
---
HINT: Compare les nombres avec les opérateurs >, <, ==
HINT: 15 est-il supérieur à 10 ? Utilise >
HINT: 20 est-il égal à 20 ? Utilise ==
HINT: "Python" est-il égal à "Python" ? Utilise ==
"""

# Complète ces comparaisons
est_plus_grand = ???  # 15 > 10 (devrait être True)
est_egal = ???        # 20 == 20 (devrait être True)
est_different = ???   # 5 != 3 (devrait être True)
texte_egal = ???      # "Python" == "Python" (devrait être True)

# Tests
assert est_plus_grand == True, "15 est bien supérieur à 10"
assert est_egal == True, "20 est bien égal à 20"
assert est_different == True, "5 est bien différent de 3"
assert texte_egal == True, '"Python" est bien égal à "Python"'

print("✓ Toutes les comparaisons sont correctes !")
print(f"  15 > 10 : {est_plus_grand}")
print(f"  20 == 20 : {est_egal}")
print(f"  5 != 3 : {est_different}")
print(f"  'Python' == 'Python' : {texte_egal}")