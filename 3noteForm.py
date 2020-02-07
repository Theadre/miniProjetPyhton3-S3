from mydb import Db
import pymysql
import cgi
# # import pymysql
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

db = Db()
tableName = 'note'
note = form.getvalue("note")
id_etudiant = form.getvalue("id_etudiant")
id_cours = form.getvalue("id_cours")

# add record
if str(note) != "None" and str(id_etudiant) != "None" and str(id_cours) != "None":
    db.updateQuery(f"insert into {tableName} values (null, '{id_etudiant}', '{id_cours}', '{note}')")

# get all
listEtudiant = db.getQuery(f'select * from Etudiant')
listEtudiantHtml = ''
for e in listEtudiant :
    listEtudiantHtml += f'{e[0]}. {e[1]} {e[2]} ({e[2]})<br>'

listCours = db.getQuery(f'select * from Cours')
listCoursHtml = ''
for e in listCours:
    listCoursHtml += f'{e[0]}. {e[1]} ({e[2]})<br>'


listNote = db.getQuery(f"""
select note, c.intitule, c.annee, e.nom, e.prenom 
from Note n 
    INNER JOIN etudiant e on n.id_etudiant = e.id
    INNER JOIN cours c on n.id_cours = c.id
""")

listNoteHtml = ''
for e in listNote:
    listNoteHtml += f"La note {e[0]} pour le cours {e[1]} ({e[2]}) a ete ajoutee pour l'etudiant {e[3]} {e[4]}<br>"
    

navbar =  open('index.py','+r').read() 
html = f"""<!DOCTYPE html>
<head>
    <title>Groupf</title>
</head>
<body>
    {navbar}
    <form action="/3noteForm.py" method="post">
        Notes a attribuees : <input type="number" name="note" value="" required/> <br>

        Liste des etdiants : <br>
        {listEtudiantHtml}
        Votre choix: <input type="number" name="id_etudiant" value=""  required/> <br>

        Liste des cours: <br>
        {listCoursHtml}
        Votre choix: <input type="number" name="id_cours" value=""  required/> <br>

        <input type="submit" name="send" value="Valider"> <br>
    </form> 
    {listNoteHtml}
</body>
</html>
"""

print(html)

