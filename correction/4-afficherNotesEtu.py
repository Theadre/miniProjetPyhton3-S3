#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db

html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Notes d'un etudiant</title>
</head>
<form action="4-validation.py" method="GET">
"""

d = Db()

html += d.get_etudiants()

html += """
    Votre choix: <input type="number" name="id_etudiant" value=""/><br>
"""

html += """
    <input type="submit" value="Valider" />
</form>
</html>
"""

print(html)
