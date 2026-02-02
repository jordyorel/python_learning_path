"""
EXERCISE: 018
TITLE: QUIZ 3 - Fondamentaux (Difficile)
DIFFICULTY: 3
CONCEPTS: quiz, synthesis, all concepts
---
Quiz de synthèse combinant tous les concepts du chapitre 1.
Valide ta compréhension avant de passer au chapitre 2.

Ce quiz teste TOUS les concepts :
- Variables, types, conversions
- Opérations mathématiques et logiques
- Chaînes, listes, tuples
- Conditions et méthodes
---
HINT: Combine plusieurs concepts appris
HINT: Lis bien chaque question
HINT: Teste ton code mentalement avant de valider
"""

# Question 1 : Conversion et calcul
age_texte = "25"
age_suivant = ???  # Convertis en int et ajoute 1

# Question 2 : Manipulation de chaîne
nom_complet = "  ALICE MARTIN  "
nom_propre = ???  # Nettoie, met en minuscules, puis en capitalize
# Résultat attendu : "Alice martin"

# Question 3 : Liste et condition
scores = [45, 78, 92, 65, 88]
meilleur_score = ???  # Accède au score maximum (index 2)
est_excellent = ???  # True si meilleur_score >= 90

# Question 4 : Logique complexe
temperature = 25
est_ensoleille = True
bonne_journee = ???  # True si temp entre 20 et 30 ET ensoleillé

# Question 5 : Tuple et déstructuration
coordonnees = (10, 20)
x, y = ???  # Déstructure le tuple (extrais x et y)

# Question 6 : Méthodes et f-strings
fruits = ["pomme", "banane"]
???  # Ajoute "orange" à la liste
phrase = ???  # f"J'ai {len(fruits)} fruits"

# Tests
assert age_suivant == 26, "Q1: Conversion et calcul"
assert nom_propre == "Alice martin", "Q2: Nettoyage et formatage"
assert meilleur_score == 92, "Q3a: Maximum de la liste"
assert est_excellent == True, "Q3b: 92 >= 90"
assert bonne_journee == True, "Q4: Logique combinée"
assert x == 10 and y == 20, "Q5: Déstructuration"
assert fruits == ["pomme", "banane", "orange"], "Q6a: Ajout à la liste"
assert phrase == "J'ai 3 fruits", "Q6b: F-string avec len()"

print("QUIZ 3 RÉUSSI ! (8/8)")
print("CHAPITRE 1 TERMINÉ !")
print("Tu es prêt(e) pour le Chapitre 2 : Boucles")