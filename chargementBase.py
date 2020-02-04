#!/usr/bin/python3

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
   prenom  CHAR(20) NOT NULL,
   nom  CHAR(20),
   age INT)"""
cursor.execute(sql)
db.commit()
print("Table etudiants created successfully<br>")



# Creer la table cours
sql = """CREATE TABLE cours (
   intitule  CHAR(20) NOT NULL,
   annee INT)"""
cursor.execute(sql)
db.commit()
print("Table cours created successfully<br>")



# Creer la table notes
sql = """CREATE TABLE notes (
   note  INT NOT NULL,
   id_etudiant  CHAR(20) NOT NULL,
   id_cours  CHAR(20) NOT NULL
   )"""
cursor.execute(sql)
db.commit()
print("Table notes created successfully<br>")


# disconnect from server
db.close()