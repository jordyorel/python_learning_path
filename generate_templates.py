#!/usr/bin/env python3
"""
Script pour générer les fichiers templates à partir des exercices actuels.
Les templates contiennent les ??? et servent de "versions propres" des exercices.
"""

import os
import re
import glob
from pathlib import Path

EXERCISES_DIR = "exercises"
TEMPLATES_DIR = "templates"

def extract_code_without_solutions(file_path):
    """Extrait le code en remplaçant les solutions par ???"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trouve le docstring
    if '"""' not in content:
        return content
    
    start = content.find('"""')
    end = content.find('"""', start + 3)
    if end == -1:
        return content
    
    docstring = content[:end + 3]
    code_part = content[end + 3:]
    
    # Le code_part contient les solutions, on garde juste le docstring
    # et on crée un template vierge
    return docstring + "\n\n# À compléter\n???\n"

def generate_templates():
    """Génère tous les fichiers templates"""
    exercise_files = sorted(glob.glob(os.path.join(EXERCISES_DIR, "*.py")))
    
    if not exercise_files:
        print(f"❌ Aucun exercice trouvé dans {EXERCISES_DIR}/")
        return
    
    for ex_file in exercise_files:
        ex_path = Path(ex_file)
        template_path = Path(TEMPLATES_DIR) / ex_path.name
        
        # Copie le fichier (pour maintenant, les templates = les exercices)
        with open(ex_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Template créé: {template_path}")
    
    print(f"\n✨ {len(exercise_files)} templates générés dans {TEMPLATES_DIR}/")

if __name__ == "__main__":
    generate_templates()
