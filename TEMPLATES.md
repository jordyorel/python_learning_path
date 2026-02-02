# 📂 Architecture des Templates

## 🎯 Philosophie

Le projet utilise une **séparation claire** entre :
- **`templates/`** → Versions "propres" de chaque exercice (templates d'origine)
- **`exercises/`** → Fichiers que l'apprenant modifie et complète

Cette architecture prévient les apprenants de copier accidentellement des solutions dans un fichier exercice.

## 📊 Structure

```
pythonlings/
├── exercises/               ← Exercices que l'utilisateur complète
│   ├── 001_hello.py        ← Modifie ce fichier
│   ├── 002_variables.py
│   ├── ...
│   └── 018_quiz_basics_hard.py
│
├── templates/              ← Copies de référence (source de vérité)
│   ├── 001_hello.py        ← Ne modifie PAS ceci
│   ├── 002_variables.py
│   ├── ...
│   └── 018_quiz_basics_hard.py
│
├── progress.json           ← Suivi de progression
├── generate_templates.py   ← Script pour générer les templates
└── README.md
```

## 🔄 Flux de travail

### 1️⃣ Initialisation (première fois)

```bash
# Les templates sont générés automatiquement
python3 generate_templates.py

# Maintenant tu as des copies de référence dans templates/
```

### 2️⃣ Résoudre un exercice

```bash
# Édite exercises/001_hello.py
# Remplace les ??? par du code

# Exécute
python3 main.py

# Si erreur, tu peux voir la solution
python3 main.py --show-solution
```

### 3️⃣ Recommencer un exercice

```bash
# Si tu veux recommencer l'exercice 5
python3 main.py --reset-exercise 5

# Le fichier exercises/005_*.py est restauré depuis templates/
# Et retiré de la progression
```

### 4️⃣ Recommencer complètement

```bash
# Réinitialise TOUS les exercices et la progression
python3 main.py --reset
```

## 🛠️ Ajouter un nouvel exercice

### Étape 1 : Créer le fichier dans `exercises/`

```bash
# Crée exercises/019_mon_exercice.py
# (Voir CONTRIBUTING.md pour le template)
```

### Étape 2 : Générer le template

```bash
# Génère le fichier template correspondant
python3 generate_templates.py

# Cela crée templates/019_mon_exercice.py
```

### Étape 3 : Tester

```bash
# Test avec le runner
python3 main.py

# Complète ton exercice localement
# Puis continue...
```

## 🔒 Avantages de cette architecture

| Problème | Solution |
|----------|----------|
| L'apprenant accidentellement divulgue la solution | Les solutions sont dans `templates/`, pas en évidence |
| On perd la version d'origine d'un exercice | `generate_templates.py` crée des copies de référence |
| Difficile de recommencer | `--reset-exercise N` restaure depuis le template |
| Pas de versioning clair | Les templates servent de "source de vérité" |
| Confusion sur les fichiers à modifier | Clair : modifie `exercises/`, pas `templates/` |

## 📝 Bonnes pratiques

### ✅ À faire

- ✅ Modifie les fichiers dans `exercises/`
- ✅ Consulte les fichiers dans `templates/` si tu veux vérifier
- ✅ Utilise `--reset-exercise N` pour recommencer un exercice
- ✅ Utilise `--reset` pour tout recommencer
- ✅ Exécute `generate_templates.py` après avoir ajouté un nouvel exercice

### ❌ À ne pas faire

- ❌ Ne modifie pas les fichiers dans `templates/`
- ❌ Ne copie pas les solutions de `templates/` à la main
- ❌ Ne désactive pas le système de templates

## 🔧 Maintenance

### Mettre à jour les templates

Si tu ajoutes de nouveaux exercices, mets à jour les templates :

```bash
# Regénère tous les fichiers templates
python3 generate_templates.py

# Vérifie que tout est correct
git diff templates/
```

### Vérifier la cohérence

```bash
# Assure-toi que chaque exercice a un template correspondant
ls exercises/ | wc -l  # Nombre d'exercices
ls templates/  | wc -l  # Nombre de templates (doit être pareil)
```

## 🎓 Flux pour l'apprenant

```
Démarre                    
    ↓
python3 main.py            
    ↓                     
Édite exercises/XXX.py     
Remplace ??? par code      
    ↓                     
python3 main.py            
    ↓                     
Erreur? Oui → Voir indices  
    ↓       ↓              
   Non   python3 main.py --show-solution
    ↓       ↓              
    ↓   Édite + relance    
    ↓       ↓              
   Succès! ✅              
    ↓                     
Prochain exo               
```

---

**Cette architecture garantit une expérience saine pour les apprenants ! 🎯**
