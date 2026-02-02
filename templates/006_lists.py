"""
EXERCISE: 006
TITLE: Listes - Introduction
DIFFICULTY: 2
CONCEPTS: lists, indexing, len
---
Une liste contient plusieurs éléments entre crochets :

    fruits = ["pomme", "banane", "orange"]
    nombres = [1, 2, 3, 4, 5]

Accéder aux éléments (l'index commence à 0) :
    fruits[0]   → "pomme" (premier élément)
    fruits[1]   → "banane" (deuxième élément)
    fruits[-1]  → "orange" (dernier élément)

Longueur d'une liste :
    len(fruits)  → 3

Crée et manipule des listes.
---
HINT: Une liste utilise des crochets []
HINT: Les éléments sont séparés par des virgules
HINT: L'index 0 est le premier élément
HINT: ma_liste = ["chat", "chien", "oiseau"]
"""

# Crée une liste avec 4 couleurs
couleurs = ???  # ["rouge", "bleu", "vert", "jaune"]

# Accède au premier élément
premiere_couleur = ???

# Accède au dernier élément
derniere_couleur = ???

# Compte le nombre d'éléments
nombre_couleurs = ???

# Tests
assert isinstance(couleurs, list), "couleurs doit être une liste"
assert len(couleurs) == 4, "couleurs doit contenir 4 éléments"
assert premiere_couleur == couleurs[0], "premiere_couleur doit être le premier élément"
assert derniere_couleur == couleurs[-1], "derniere_couleur doit être le dernier élément"
assert nombre_couleurs == 4, "nombre_couleurs doit être 4"

print("✓ Parfait ! Tu maîtrises les bases des listes !")
print(f"  Liste : {couleurs}")
print(f"  Première couleur : {premiere_couleur}")
print(f"  Dernière couleur : {derniere_couleur}")
print(f"  Nombre de couleurs : {nombre_couleurs}")