from mydb import Db
import pymysql
import cgi
# # import pymysql
form = cgi.FieldStorage()
tableName = 'note'
print("Content-type: text/html; charset=utf-8\n")


db = Db()
id_etudiant = form.getvalue("id_etudiant")
listNotePourEtudiantHtml = ''
etudiantSelectionne = []
if str(id_etudiant) != "None":

    e = db.getOneQuery(f"select * from etudiant where id = {id_etudiant}")

    listNotePourEtudiantHtml += f'Note de {e[1]} {e[2]} ({e[3]} ans): <br>'

    listNote = db.getQuery(f"""
    select c.intitule, c.annee, note
    from note n
        INNER JOIN etudiant e on n.id_etudiant = e.id
        INNER JOIN cours c on n.id_cours = c.id
    where id_etudiant = {id_etudiant}
    """)

    
    for e in listNote:
        listNotePourEtudiantHtml += f"- {e[0]} ({e[1]}): {e[2]}<br>"



# get all
listEtudiant = db.getQuery(f'select * from Etudiant')
listEtudiantHtml = ''
for e in listEtudiant :
    listEtudiantHtml += f'{e[0]}. {e[1]} {e[2]} ({e[2]})<br>'

navbar =  open('navbar.html','+r').read() 
html = f"""<!DOCTYPE html>
<head>
    <title>Groupe f</title>
</head>
<body>
    {navbar}
    <form action="/4noteAffiche.py" method="post">
        Liste des etudiants : <br>
        {listEtudiantHtml}
        Votre choix: <input type="number" name="id_etudiant" value=""  required/> <br>

        <input type="submit" name="send" value="Valider"> <br><br>

        {listNotePourEtudiantHtml}

    </form> 
</body>
</html>
"""
print(html)

