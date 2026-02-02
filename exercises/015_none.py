"""
EXERCISE: 015
TITLE: La valeur None
DIFFICULTY: 1
CONCEPTS: None, null
---
None représente l'absence de valeur (comme null/nil dans d'autres langages) :

    resultat = None  # Pas encore de valeur

Pour tester None :
    if resultat is None:
        print("Pas de résultat")
    
    if resultat is not None:
        print("Il y a un résultat")
---
HINT: None s'écrit avec une majuscule
HINT: Utilise 'is None' pour tester
HINT: Utilise 'is not None' pour l'inverse
"""

valeur = None

# Teste si la valeur est None
est_vide = ???  # valeur is None

# Assigne une nouvelle valeur
valeur = 42

# Teste si la valeur n'est plus None
a_valeur = ???  # valeur is not None

# Tests
assert est_vide == True, "None devrait être détecté"
assert a_valeur == True, "42 n'est pas None"

print("✓ Tu comprends None !")