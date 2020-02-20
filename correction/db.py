import pymysql


class Db(object):
    user = "test"
    passwd = "test"
    dbName = "DbPythonSem3"
    dbHost = "localhost"

    def createDb(self):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd)
            conn.cursor().execute("create database " + self.dbName)
            return "Database " + self.dbName + " created successfully<br>"
        except:
            return "Error creating database<br>"

    def createTables(self):
        html = ""
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = """CREATE TABLE etudiants(
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                    prenom CHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
                    nom CHAR(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL UNIQUE,
                    age INT NOT NULL)"""
                cur.execute(sql)
                html += "Table etudiants created successfully<br>"

                sql = """CREATE TABLE cours(
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    intitule CHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
                    annee INT NOT NULL)"""
                cur.execute(sql)
                html += "Table cours created successfully<br>"

                sql = """CREATE TABLE notes(
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    note INT NOT NULL,
                    id_etudiant INT NOT NULL,
                    id_cours INT NOT NULL,
                    FOREIGN KEY (id_etudiant) REFERENCES etudiants(id),
                    FOREIGN KEY (id_cours) REFERENCES cours(id) )"""
                cur.execute(sql)
                html += "Table notes created successfully<br>"
        except:
            html += "An error occurred when creating tables<br>"
        return html

    def ajout_etudiant (self, prenom, nom, age):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = "INSERT INTO etudiants (prenom, nom, age) VALUES \
                    ('%s', '%s', '%d')" % (prenom, nom, age)
                cur.execute(sql)
                conn.commit()
                return "L'etudiant " + prenom + " " + nom + " (" + \
                    str(age) + " ans) a ete ajoute<br>"
        except:
            return "Erreur ajout etudiant<br>"

    def ajout_cours (self, intitule, annee):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = "INSERT INTO cours (intitule, annee) VALUES \
                    ('%s', '%d')" % (intitule, annee)
                cur.execute(sql)
                conn.commit()
                return "Le cours " + intitule + " (" + \
                    str(annee) + ") a ete ajoute<br>"
        except:
            return "Erreur ajout cours<br>"

    def ajout_note (self, note, etuId, coursId):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = "INSERT INTO notes (note, id_etudiant, id_cours) VALUES \
                    ('%d', '%d', '%d')" % (note, etuId, coursId)
                cur.execute(sql)
                conn.commit()
                return "La note " + str(note) + " pour le cours " + str(coursId) + \
                       " a ete ajoutee pour l'etudiant " + str(etuId) + "<br>"
        except:
            return "Erreur ajout etudiant<br>"

    def get_etudiants(self):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = "SELECT id, prenom, nom, age FROM etudiants"
                cur.execute(sql)
                results = cur.fetchall()
                html = ""
                for row in results:
                    html += ("%d. %s %s (%d ans)<br>") % (row[0], row[1], row[2], row[3])
                return html
        except:
            return "Erreur affichage etudiants<br>"

    def get_cours(self):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = "SELECT id, intitule, annee FROM cours"
                cur.execute(sql)
                results = cur.fetchall()
                html = ""
                for row in results:
                    html += ("%d. %s (%d)<br>") % (row[0], row[1], row[2])
                return html
        except:
            return "Erreur affichage cours<br>"

    def get_notes_by_etudiant_id(self, etuID):
        html = "Notes de " + self.get_etudiant_by_id(etuID) + ":<br>"
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = ("SELECT note, id_cours FROM notes WHERE id_etudiant = %d") % (etuID)
                cur.execute(sql)
                results = cur.fetchall()
                for row in results:
                    html += ("%d - %s<br>") % (row[0], self.get_cours_by_id(int(row[1])))
                return html
        except:
            return "Erreur affichage notes etudiant<br>"

    def get_etudiant_by_id(self, etuID):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = ("SELECT prenom, nom, age  FROM etudiants WHERE id = %d") % (etuID)
                cur.execute(sql)
                row = cur.fetchone()
                return ("%s %s (%d ans)") % (row[0], row[1], row[2])
        except:
            return "Erreur affichage etudiant<br>"

    def get_cours_by_id(self, coursID):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = ("SELECT intitule, annee FROM cours WHERE id = %d") % (coursID)
                cur.execute(sql)
                row = cur.fetchone()
                return ("%s (%d)") % (row[0], row[1])
        except:
            return "Erreur affichage cours<br>"

    def get_notes_triees_by_cours_id(self, coursID):
        try:
            html = "Notes triees du cours " + self.get_cours_by_id(coursID) + ":<br>"
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = ("SELECT note, id_etudiant FROM notes WHERE id_cours = %d") % (coursID)
                cur.execute(sql)
                results = cur.fetchall()
                dicoNotes = {}
                for row in results:
                    dicoNotes[int(row[1])] = int(row[0])
                s = [(k, dicoNotes[k]) for k in sorted(dicoNotes, key=dicoNotes.get, reverse=True)]
                for key, value in s:
                    html += self.get_etudiant_by_id(key) + " - " + str(value) + "<br>"
                return html
        except:
            return "Erreur affichage notes cours<br>"

    def delete_cours_by_cours_id(self, coursID):
        try:
            conn = pymysql.connect(self.dbHost, self.user, self.passwd, self.dbName)
            with conn:
                cur = conn.cursor()
                sql = ("DELETE FROM notes WHERE id_cours = %d") % (coursID)
                cur.execute(sql)
                conn.commit()
                sql = ("DELETE FROM cours WHERE id = %d") % (coursID)
                cur.execute(sql)
                conn.commit()

                return "Le cours " + str(coursID) + " et les notes associees ont ete supprimees<br>"
        except:
            return "Erreur affichage notes cours<br>"
