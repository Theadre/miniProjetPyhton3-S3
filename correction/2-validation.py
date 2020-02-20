#!/usr/bin/python3
# -*- coding: utf-8 -*

from db import Db
import cgi


html = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html"; charset="UTF-8">
    <title>Ajout d'un etudiant</title>
</head>
<body>
"""

form = cgi.FieldStorage()
if str(form.getvalue('prenom')) == "None" or str(form.getvalue('nom')) == "None" or \
        str(form.getvalue('age')) == "None":
    html += "Erreur de saisie dans le formulaire"
else:
    # print(form.getvalue("name"))
    d = Db()
    html += d.ajout_etudiant(str(form.getvalue("prenom")), str(form.getvalue("nom")), \
                             int(form.getvalue("age")))

html += """
<br><a href=\"index.py\">Retour au menu principal</a>
</body>
</html>
"""

print(html)
