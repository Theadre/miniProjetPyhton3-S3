#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db

html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Supprimer un cours</title>
</head>
<form action="6-validation.py" method="GET">
"""

d = Db()

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
