"""
EXERCISE: 009
TITLE: Conversion de types
DIFFICULTY: 1
CONCEPTS: type conversion, int, str, float
---
Conversions entre types :

    int("42")     → 42 (chaîne vers entier)
    str(42)       → "42" (entier vers chaîne)
    float("3.14") → 3.14 (chaîne vers décimal)
    int(3.9)      → 3 (tronque le décimal)

Complète les conversions.
---
HINT: Utilise int() pour convertir en entier
HINT: Utilise str() pour convertir en chaîne
HINT: Utilise float() pour convertir en décimal
HINT: texte_vers_nombre = int("100")
"""

# Convertis ces valeurs
texte_vers_nombre = ???  # "100" → 100
nombre_vers_texte = ???  # 50 → "50"
texte_vers_decimal = ???  # "3.14" → 3.14
decimal_vers_entier = ???  # 7.8 → 7

# Tests
assert texte_vers_nombre == 100 and isinstance(texte_vers_nombre, int)
assert nombre_vers_texte == "50" and isinstance(nombre_vers_texte, str)
assert texte_vers_decimal == 3.14 and isinstance(texte_vers_decimal, float)
assert decimal_vers_entier == 7 and isinstance(decimal_vers_entier, int)

print("Conversions réussies !")