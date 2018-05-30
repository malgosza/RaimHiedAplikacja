import sqlite3
# baza.db
baza=sqlite3.connect('baza.db')
baza.row_factory=sqlite3.Row
c=baza.cursor()

c.execute('DROP TABLE IF EXISTS pytania')
c.execute("CREATE TABLE pytania(id integer primary key,trescPytania varchar(100))")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Płeć')")
# c.execute("INSERT INTO pytania(trescPytania) VALUES('Wiek')")
# c.execute("INSERT INTO pytania(trescPytania) VALUES('Waga')")
# c.execute("INSERT INTO pytania(trescPytania) VALUES('Wzrost')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Jak oceniasz swój sposób odżywiania?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Jak często uprawiasz sport?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy prowadzisz stresujący tryb życia')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy palisz papierosy nałogowo?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy pijesz alkohol?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy korzystasz z innych używek?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy masz problemy z układem krążeniowym')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy w Twojej rodzinie ma ktoś problemy z układem krążeniowym')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy przeszedłeś chorobę nowotworową?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy ktoś z rodziny przeszedł chorobę nowotworową?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy w rodzinie bywały przypadki zachorowań na Alzheimera?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Czy doznałeś kiedyś urazu głowy?')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Wykształcenie')")



c.execute('DROP TABLE IF EXISTS odpowiedzi')
c.execute("CREATE TABLE odpowiedzi(id integer primary key, idPytania integer, trescOdpowiedzi varchar(30), wagaOdpowiedzi integer )")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(1,'Kobieta',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(1,'Mężczyzna',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(2,'Bardzo dobrze',1)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(2,'Poprawnie',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(2,'Mogłoby być lepiej',3)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(2,'Źle',4)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(3,'Codziennie',1)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(3,'3-5 razy w tygodniu',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(3,'2-3 razy w tygodniu',3)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(3,'Sporadycznie',4)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(3,'Nigdy, nie mam czasu na trening',5)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(4,'Zdecydowanie tak',4)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(4,'Raczej tak',3)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(4,'Raczej nie',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(4,'Zdecydowanie nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(5,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(5,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(6,'Zdecydowanie nie',1)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(6,'Piję tylko w wyjątkowych sytuacjach',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(6,'Piję zawsze kiedy mam okazję',3)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(6,'Piję nałogowo',4)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(7,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(7,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(8,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(8,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(9,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(9,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(10,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(10,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(11,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(11,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(12,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(12,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(13,'Tak',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(13,'Nie',1)")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(14,'podstawowe nieukończone i bez wykształcenia',7)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(14,'podstawowe ukończone',6)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(14,'zasadnicze zawodowe',5)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(14,'średnie zawodowe',4)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(14,'średnie ogólnokształcące',3)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(14,'policealne',2)")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi,wagaOdpowiedzi) VALUES(14,'wyższe',1)")

c.execute('DROP TABLE IF EXISTS choroby')
c.execute("CREATE TABLE choroby(id integer primary key, nazwaChoroby varchar(30), gornaGranica integer, dolnaGranica integer, zalecenia varchar(70))")
c.execute("INSERT INTO choroby(nazwaChoroby, gornaGranica, dolnaGranica, zalecenia) VALUES('Nie wypełniłeś ankiety :(',0,13,'Nie możemy Ci pomóc zdiagnozować schorzenia')")
c.execute("INSERT INTO choroby(nazwaChoroby, gornaGranica, dolnaGranica, zalecenia) VALUES('Zawał',15,25,'Warto zwrócić większą uwagę na dietę, więcej się ruszać i mniej stresować')")
c.execute("INSERT INTO choroby(nazwaChoroby, gornaGranica, dolnaGranica, zalecenia) VALUES('Choroba ukladu krazenia',26,44,'Więcej się ruszaj i pamiętaj, że odpowiednia dieta to podstawa')")
c.execute("INSERT INTO choroby(nazwaChoroby, gornaGranica, dolnaGranica, zalecenia) VALUES('Alzheimer',45,65,'Jesteś w grupie zagrożenia, ale pamiętaj, że jeszcze wszystko można zmienić! Bądź aktywny! Rozwijaj swoje hobby, wicz dużó na świeżym powietrzu')")
c.execute("INSERT INTO choroby(nazwaChoroby, gornaGranica, dolnaGranica, zalecenia) VALUES('Jestes zdrowy',66,200,'Gratulacje! Jesteś okazem zdrowia! Warto jednak pamiętać, że wszystko, co robimy wpływa na nasze zdrowie ')")

# c.execute("SELECT * FROM pytania JOIN odpowiedzi ON pytania.id=odpowiedzi.idPytania WHERE pytania.trescPytania='Płeć' AND odpowiedzi.trescOdpowiedzi='Kobieta'")
# result=32
# c.execute("SELECT zalecenia FROM choroby WHERE choroby.gornaGranica<= 0 AND choroby.dolnaGranica>= 0")
# x=dict(c.fetchone())['zalecenia']
# print(x)
#
# c.execute("SELECT nazwaChoroby FROM choroby WHERE choroby.gornaGranica<= 0 AND choroby.dolnaGranica>= 0")
# y=dict(c.fetchone())['nazwaChoroby']
# print(y)

baza.commit()
c.close()
baza.close()

