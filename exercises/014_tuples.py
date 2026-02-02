"""
EXERCISE: 014
TITLE: Tuples (immuables)
DIFFICULTY: 1
CONCEPTS: tuples, immutability
---
Un tuple est comme une liste MAIS immuable (non modifiable) :

    coordonnees = (10, 20)  # Parenthèses
    x = coordonnees[0]      → 10

Différences avec les listes :
    - Tuples : () et immuables
    - Listes : [] et modifiables

Les tuples sont plus rapides et sûrs pour les données fixes.
---
HINT: Un tuple utilise des parenthèses ()
HINT: Accès par index comme les listes
HINT: point = (5, 10)
HINT: x = point[0], y = point[1]
"""

# Crée un tuple avec deux coordonnées
point = ???  # (5, 10)

# Extrais x et y
x = ???
y = ???

# Tests
assert isinstance(point, tuple), "point doit être un tuple"
assert point == (5, 10), "point doit être (5, 10)"
assert x == 5 and y == 10, "x=5, y=10"

print(f"Coordonnées : ({x}, {y})")