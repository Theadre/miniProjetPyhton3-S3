#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db
import cgi


html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Ajout d'une note</title>
</head>
<body>
"""

form = cgi.FieldStorage()
if str(form.getvalue('note')) == "None" or str(form.getvalue('id_etudiant')) == "None" or \
        str(form.getvalue('id_cours')) == "None":
    html += "Erreur de saisie dans le formulaire"
else:
    # print(form.getvalue("name"))
    d = Db()
    html += d.ajout_note(int(form.getvalue("note")), int(form.getvalue("id_etudiant")), \
                             int(form.getvalue("id_cours")))

html += """
<br><a href=\"index.py\">Retour au menu principal</a>
</body>
</html>
"""

print(html)
