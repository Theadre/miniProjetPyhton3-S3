from mydb import Db
import pymysql
import cgi

form = cgi.FieldStorage()
tableName = 'etudiant'
print("Content-type: text/html; charset=utf-8\n")

db = Db()
prenom = form.getvalue("prenom")
nom = form.getvalue("nom")
age = form.getvalue("age")

# add record
if str(prenom) != "None" and str(nom) != "None" and str(age) != "None":
    db.updateQuery(f"insert into {tableName} values (null, '{nom}', '{prenom}', '{age}')")


# get all
list = db.getQuery(f'select * from {tableName}')

listHtml = ''
for row in list:
    listHtml += f'nom : {row[1]}, prenom {row[2]}, age {row[3]} <br>'

navbar =  open('index.py','+r').read() 
        

html = f"""<!DOCTYPE html>
<head>
    <title>Groupf</title>
</head>
<body>
    {navbar}
    <form action="/2etudiantForm.py" method="post">
        Prenom : <input type="text" name="prenom" value="" required/>  <br>
        Nom : <input type="text" name="nom" value="" required/> <br>
        Age : <input type="number" name="age" value="" required/> <br>
        <input type="submit" name="send" value="Enregistrer"> <br>
    </form> 
    {listHtml}
</body>
</html>
"""

print(html)

