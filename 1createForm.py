from mydb import Db
from config import Config
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")




# sql

coursSql = f"""
create table if not EXISTS Cours(
    id int primary key auto_increment,
    intitule text not null,
    annee int not null
);
"""

etudiantSql = f"""
create table if not EXISTS Etudiant(
    id int primary key auto_increment,
    nom text not null,
    prenom text not null,
    age int not null
);
"""

noteSql = f"""
create table if not EXISTS Note(
    id int primary key auto_increment,
    id_etudiant int not null,
    id_cours int not null,
    note int not null,
    FOREIGN KEY (id_etudiant) REFERENCES Etudiant(id),
    FOREIGN KEY (id_cours) REFERENCES Cours(id)
);
"""
navbar =  open('navbar.html','+r').read() 

print(navbar)


db = Db()


    
# 2 - create
# db.updateDataBase(f'DROP DATABASE IF EXISTS {Config.db};')
db.updateDataBase(f'create database if not EXISTS {Config.db};')
db.updateDataBase(f'use {Config.db};')
print(f'database {Config.db} created successfully<br>')

# 1- drop if existe

db.updateTable('DROP TABLE IF EXISTS note')
db.updateTable('DROP TABLE IF EXISTS etudiant')
db.updateTable('DROP TABLE IF EXISTS cours')

db.updateTable(etudiantSql)
print('Table etudiant created successfully<br>')

db.updateTable(coursSql)
print('Table cours created successfully<br>')

db.updateTable(noteSql)
print('Table note created successfully<br>')

print('<br><br>')

# 3 - insert

db.updateQuery("INSERT INTO etudiant(prenom, nom, age) VALUES ('Mark', 'Zuckerberg', 34), ('Bill', 'Gates', 63)")
list1 = db.getQuery(f"select * from etudiant")
[print(f"L'etudiant {e[1]} {e[2]} ({e[3]} ans) a ete ajoute<br>") for e in list1]

print('<br>')


db.updateQuery("INSERT INTO cours(intitule, annee) VALUES ('DeepLearning', 2018), ('Python', 2010)")
list2 = db.getQuery(f"select * from cours")
[print(f"Le cours  {e[1]} ({e[2]} ans) a ete ajoute<br>") for e in list2]

print('<br>')

db.updateQuery("INSERT INTO note(id_etudiant, id_cours, note) VALUES (1, 1, 15), (2, 2, 14), (1, 2, 17)")

list3 = db.getQuery(f"""
    select note, c.intitule, e.nom, e.prenom
    from note n
        INNER JOIN etudiant e on n.id_etudiant = e.id
        INNER JOIN cours c on n.id_cours = c.id
    """)
    
[print(f"La note {e[0]} pour le cours {e[1]} ({e[3]} ans)<br>") for e in list3]
    
