# coding: utf-8

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

menu = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
  
</head>
<body>
    <p><a href="chargementBase.py">1. Creer et peupler la base</a></p>
    <p><a href="etudiantAjout.py">2. Ajouter un etudiant</a></p>
    <p><a href="noteAjout.py">3. Ajouter une note</a></p>
    <p><a href="etudiantAfficher.py">4. Afficher les notes d'un etudiant</a></p>
    <p><a href="noteAfficher.py">5. Afficher les notes triees d'un cours</a></p>
    <p><a href="coursSupprimer.py">6. Supprimer un cours</a></p>
</body>
</html>
"""

print(menu)


