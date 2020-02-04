#!/usr/bin/python3

from models.db import Db
import pymysql
import cgi 
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

menu = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
  
</head>
<body>

</body>
</html>
"""

print(menu)

# Connection MySQL
db = pymysql.connect("localhost","root","")
cursor = db.cursor()


# Supprimer la base si existante
cursor.execute("DROP DATABASE IF EXISTS groupef")


# Creer la base de donnees
sql = """CREATE DATABASE groupef"""
cursor.execute(sql)
db.commit()
print("Database groupef created successfully<br>")
db.close()


# Connection MySQL
db = pymysql.connect("localhost","root","", "groupef")
cursor = db.cursor()


# Creer la table etudiant
sql = """CREATE TABLE etudiant (
   id_etudiant INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
   prenom  CHAR(20) NOT NULL,
   nom  CHAR(20) NOT NULL,
   age INT NOT NULL)"""
cursor.execute(sql)
db.commit()
print("Table etudiants created successfully<br>")



# Creer la table cours
sql = """CREATE TABLE cours (
   id_cours INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
   intitule  CHAR(20) NOT NULL,
   annee INT)"""
cursor.execute(sql)
db.commit()
print("Table cours created successfully<br>")



# Creer la table notes
sql = """CREATE TABLE notes (
   note  INT NOT NULL,
   id_etudiant  INT NOT NULL,
   id_cours  INT NOT NULL
   )"""
cursor.execute(sql)
db.commit()
print("Table notes created successfully<br>")



# Inserer des etudiants
sql = """INSERT INTO etudiants(prenom, nom, age) VALUES ('Mark', 'Zuckerberg', 34)"""
sql = """INSERT INTO etudiants(prenom, nom, age) VALUES ('Bill', 'Gates', 63)"""
print("L'etudiant Mark ZuckerBerg (34 ans) a ete ajoute<br>")
print("L'etudiant Bill Gates (63 ans) a ete ajoute<br>")

sql = """INSERT INTO cours(intitule, annee) VALUES ('DeepLearning', 2018)"""
sql = """INSERT INTO cours(intitule, annee) VALUES ('Python', 2010)"""
print("Le cours DeepLearning (2018) a ete ajoute<br>")
print("Le cours Python (2010) a ete ajoute<br>")

sql = """INSERT INTO notes(id_etudiant, id_cours, note) VALUES (1, 1, 15)"""
sql = """INSERT INTO notes(id_etudiant, id_cours, note) VALUES (2, 2, 14)"""
sql = """INSERT INTO notes(id_etudiant, id_cours, note) VALUES (1, 2, 17)"""
print("la note La note 15 pour le cours DeepLearning a ete ajoutee pour Mark Zuckerberg")
print("la note La note 14 pour le cours Python a ete ajoutee pour Bill Gates")
print("la note La note 17 pour le cours Python a ete ajoutee pour Mark Zuckerberg")


cursor.execute(sql)
db.commit()




# disconnect from server
db.close()