from mydb import Db
import pymysql
import cgi
# # import pymysql
form = cgi.FieldStorage()
tableName = 'note'
print("Content-type: text/html; charset=utf-8\n")

db = Db()
id_cours = form.getvalue("id_cours")
listNoteTrieeHtml = ''
courSelectionneeHtml = ''

if str(id_cours) != "None":

    e = db.getOneQuery(f"select * from cours where id = {id_cours}")

    courSelectionneeHtml += f'Note triee du cour {e[1]} ({e[2]}): <br>'

    listNoteTriee = db.getQuery(f"""
    select e.nom, e.prenom, e.age, note
    from note n
        INNER JOIN etudiant e on n.id_etudiant = e.id
    where id_cours = {id_cours}
    order by note desc
    """)

    
    for e in listNoteTriee:
        listNoteTrieeHtml += f"- {e[0]} {e[1]} ({e[2]} ans): {e[3]}<br>"


listCours = db.getQuery(f'select * from Cours')
listCoursHtml = ''

for e in listCours:
    listCoursHtml += f'{e[0]}. {e[1]} ({e[2]})<br>'



navbar =  open('navbar.html','+r').read() 
html = f"""<!DOCTYPE html>
<head>
    <title>Groupe f</title>
</head>
<body>
    {navbar}
    <form action="/5noteTrieeAffiche.py" method="post">
         Liste des cours: <br>
        {listCoursHtml}
        Votre choix: <input type="number" name="id_cours" value=""  required/> <br>
        <input type="submit" name="send" value="Valider"> <br><br>
        {courSelectionneeHtml}
        {listNoteTrieeHtml}
    </form>
</body>
</html>
"""
print(html)