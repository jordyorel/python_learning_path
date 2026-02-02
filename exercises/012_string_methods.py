"""
EXERCISE: 012
TITLE: Méthodes de chaînes
DIFFICULTY: 1
CONCEPTS: string methods, upper, lower, strip
---
Méthodes utiles pour les chaînes :

    .upper()  → MAJUSCULES
    .lower()  → minuscules
    .strip()  → enlève les espaces aux extrémités
    .replace(ancien, nouveau)  → remplace du texte

Exemples :
    "hello".upper()     → "HELLO"
    "  test  ".strip()  → "test"
---
HINT: Utilise .upper() pour mettre en majuscules
HINT: Utilise .lower() pour mettre en minuscules
HINT: Utilise .strip() pour enlever les espaces
HINT: texte_majuscules = texte.upper()
"""

texte = "  Python  "

# Applique les méthodes
texte_majuscules = ???
texte_minuscules = ???
texte_nettoye = ???

# Tests
assert texte_majuscules == "  PYTHON  ", "Mettre en majuscules"
assert texte_minuscules == "  python  ", "Mettre en minuscules"
assert texte_nettoye == "Python", "Enlever les espaces"

print("✓ Méthodes de chaînes maîtrisées !")