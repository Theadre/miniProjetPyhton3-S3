from mydb import Db
import pymysql
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


db = Db()
id_cours = form.getvalue("id_cours")
msg = ''

if str(id_cours) != "None":

    e = db.getOneQuery(f"select * from cours where id = {id_cours}")

    r2 = db.updateQuery(f"delete from note where id_cours = {id_cours}")

    r1 = db.updateQuery(f"delete from cours where id = {id_cours}")
    
    msg = f'Le cours {e[1]} ({e[2]}) et les notes associees ont ete supprimes'

# get all
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
    <form action="/6deleteCourAffiche.py" method="post">
        Liste des cours: <br>
        {listCoursHtml}
        Votre choix: <input type="number" name="id_cours" value=""  required/> <br>

        <input type="submit" name="send" value="Valider"> <br><br>
        {msg}
    </form> 
</body>
</html>
"""
print(html)