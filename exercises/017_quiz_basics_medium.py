"""
EXERCISE: 017
TITLE: QUIZ 2 - Fondamentaux (Moyen)
DIFFICULTY: 2
CONCEPTS: quiz, lists, booleans, conditionals
---
Quiz intermédiaire sur les structures de données et conditions.

Ce quiz teste :
- Listes et indexation
- Booléens et comparaisons
- Conditions if/else
---
HINT: Relis les exercices 5-7 si besoin
HINT: Les listes commencent à l'index 0
HINT: Utilise >, <, ==, and, or pour les comparaisons
"""

# Question 1 : Crée une liste avec 3 nombres : 10, 20, 30
nombres = ???

# Question 2 : Accède au deuxième élément (index 1)
deuxieme = ???

# Question 3 : Compare si 15 est supérieur à 10 ET inférieur à 20
entre_10_et_20 = ???  # 15 > 10 and 15 < 20

# Question 4 : Condition if/else
age = 16
if ???:  # Si age >= 18
    peut_voter = True
else:
    peut_voter = False

# Question 5 : Longueur de la liste
taille = ???  # len(nombres)

# Tests
assert nombres == [10, 20, 30], "Q1: Liste incorrecte"
assert deuxieme == 20, "Q2: Le deuxième élément est 20"
assert entre_10_et_20 == True, "Q3: 15 est bien entre 10 et 20"
assert peut_voter == False, "Q4: À 16 ans, on ne peut pas voter"
assert taille == 3, "Q5: La liste contient 3 éléments"

print("QUIZ 2 RÉUSSI ! (5/5)")
print("Tu progresses bien !")