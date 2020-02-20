#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db
import cgi


html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Notes triees d'un cours</title>
</head>
<body>
"""

form = cgi.FieldStorage()
if str(form.getvalue('id_cours')) == "None":
    html += "Erreur de saisie dans le formulaire"
else:
    d = Db()
    html += d.delete_cours_by_cours_id(int(form.getvalue("id_cours")))

html += """
<br><a href=\"index.py\">Retour au menu principal</a>
</body>
</html>
"""

print(html)
