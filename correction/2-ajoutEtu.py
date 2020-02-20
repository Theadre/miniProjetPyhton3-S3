#!/usr/bin/python3
# -*- coding: utf-8 -*

html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Ajout d'un etudiant</title>
</head>
<form action="2-validation.py" method="GET">
    Prenom: <input type="text" name="prenom" value=""/><br>
    Nom: <input type="text" name="nom" value=""/><br>
    Age: <input type="number" name="age" value=""/><br>
    <input type="submit" value="Valider" />
</form>
</html>
"""

print(html)
