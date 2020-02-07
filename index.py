# coding: utf-8

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

menu = """<style>
    body{
        font-size: 1.2em;
        font-family: Arial, Helvetica, sans-serif;
    }
    nav {
        display: flex;
        background-color: black;
        padding: 15px;
        justify-content: space-around;
        flex-wrap: wrap;
    }

    nav a {
        margin-right: 10px;
        text-decoration: none;
        text-transform: uppercase;
        color: #dfdddd;
        font-weight: bold;
        font-size: medium;
        padding: 8px 0;
    }

    nav a:hover {
        color: rgb(255, 252, 78);
    }

    input {
        margin: 15px 0;
        padding: 10px;
        border-radius: 5px;
    }

    input[type=submit] {
        color: white;
        background-color: green;
        margin: 15px 0;
        text-decoration: none;
        cursor: pointer;
    }
</style>
<nav>
    <a href="1createForm.py">1 - Creer et peupler la base</a>
    <a href="2etudiantForm.py">2 - Ajouter un etudiant</a>
    <a href="3noteForm.py">3 - Ajouter une note</a>
    <a href="4noteAffiche.py">4 - Afficher les note d'un etudiant</a>
    <a href="5noteTrieeAffiche.py">5 - Afficher les notes triees d'un cours</a>
    <a href="6deleteCourAffiche.py">6 - Supprimer un cours</a>
    <a href="7courForm.py">7 - Ajouter un cours</a>
</nav>
<br>
<br>
"""

print(menu)


