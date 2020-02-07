from mydb import Db
import pymysql
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


db = Db()
tableName = 'cours'
intitule = form.getvalue("intitule")
annee = form.getvalue("annee")

if str(intitule) != "None" and str(annee) != "None":
    r = db.updateQuery(f"insert into {tableName} values (null, '{intitule}', '{annee}')")

# get all
list = db.getQuery(f'select * from {tableName}')

listHtml = ''
for row in list:
    listHtml += f'intitule : {row[1]}, annee {row[2]} <br>'

navbar =  open('index.py','+r').read() 
        
html = f"""<!DOCTYPE html>
<head>
    <title>Groupf</title>
</head>
<body>
    {navbar}
    <form action="/7courForm.py" method="post">
        <input type="text" name="intitule" value="" required/> <br>
        <input type="number" name="annee" value="" required/> <br>
        <input type="submit" name="send" value="Enregistrer"> <br>
    </form> 
    {listHtml}
</body>
</html>
"""

print(html)