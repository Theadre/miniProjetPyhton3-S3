#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db

html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Ajout d'une note</title>
</head>
<form action="3-validation.py" method="GET">
    Note a attribuer: <input type="number" name="note" value=""/><br>
"""

d = Db()

html += d.get_etudiants()

html += """
    Votre choix: <input type="number" name="id_etudiant" value=""/><br>
"""

html += d.get_cours()

html += """
    Votre choix: <input type="number" name="id_cours" value=""/><br>
"""

html += """
    <input type="submit" value="Valider" />
</form>
</html>
"""

print(html)
