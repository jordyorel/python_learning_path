"""
EXERCISE: 016
TITLE: QUIZ 1 - Fondamentaux (Facile)
DIFFICULTY: 2
CONCEPTS: quiz, variables, types, strings
---
Quiz de validation des concepts de base.
Réponds correctement aux 5 questions pour passer au quiz suivant.

Ce quiz teste :
- Variables et types
- Opérations de base
- Manipulation de chaînes
---
HINT: Relis les exercices 1-5 si nécessaire
HINT: Attention aux types (int vs string)
HINT: N'oublie pas les guillemets pour les chaînes
"""

# Question 1 : Crée une variable 'langage' avec la valeur "Python"
langage = ???

# Question 2 : Crée une variable 'version' avec la valeur 3
version = ???

# Question 3 : Calcule 7 * 6
resultat_multiplication = ???

# Question 4 : Concatène "Hello" + " " + "World"
message = ???

# Question 5 : Utilise une f-string pour créer "Python 3"
description = ???  # f"{langage} {version}"

# Tests
assert langage == "Python", "Q1: langage doit être 'Python'"
assert version == 3, "Q2: version doit être 3 (nombre)"
assert resultat_multiplication == 42, "Q3: 7 * 6 = 42"
assert message == "Hello World", "Q4: Concaténation incorrecte"
assert description == "Python 3", "Q5: F-string incorrecte"

print("QUIZ 1 RÉUSSI ! (5/5)")
print("Tu maîtrises les fondamentaux !")