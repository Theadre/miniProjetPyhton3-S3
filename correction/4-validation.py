#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db
import cgi


html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Notes d'un etudiant</title>
</head>
<body>
"""

form = cgi.FieldStorage()
if str(form.getvalue('id_etudiant')) == "None":
    html += "Erreur de saisie dans le formulaire"
else:
    d = Db()
    etuID = int(form.getvalue("id_etudiant"))
    html += d.get_notes_by_etudiant_id(etuID)

html += """
<br><a href=\"index.py\">Retour au menu principal</a>
</body>
</html>
"""

print(html)
