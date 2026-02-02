"""
EXERCISE: 011
TITLE: Opérateurs logiques
DIFFICULTY: 1
CONCEPTS: and, or, not, logic
---
Opérateurs logiques :

    and : vrai si les DEUX conditions sont vraies
    or  : vrai si AU MOINS UNE condition est vraie
    not : inverse le booléen

Exemples :
    True and True   → True
    True and False  → False
    True or False   → True
    not True        → False
---
HINT: and vérifie que les deux sont vrais
HINT: or vérifie qu'au moins un est vrai
HINT: not inverse True/False
HINT: (age >= 18) and (age < 65)
"""

age = 25
a_permis = True

# Complète ces expressions
est_adulte = ???  # age >= 18
peut_conduire = ???  # age >= 18 and a_permis
est_mineur = ???  # not (age >= 18)

# Tests
assert est_adulte == True, "25 ans est adulte"
assert peut_conduire == True, "Adulte avec permis peut conduire"
assert est_mineur == False, "25 ans n'est pas mineur"

print("Tu maîtrises les opérateurs logiques !")