#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db

html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Creation et peuplement</title>
</head>
<body>
"""

d = Db()
html += d.createDb()

html += d.createTables()

html += d.ajout_etudiant("Mark", "Zuckerberg", 34)
html += d.ajout_etudiant("Bill", "Gates", 63)

html += d.ajout_cours("Deep Learning", 2018)
html += d.ajout_cours("Python", 2010)

html += d.ajout_note(15, 1, 1)
html += d.ajout_note(14, 2, 2)
html += d.ajout_note(17, 1, 2)

html += """
<br><a href=\"index.py\">Retour au menu principal</a>
</body>
</html>
"""

print(html)