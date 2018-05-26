import sqlite3
# baza.db
baza=sqlite3.connect('baza.db')
baza.row_factory=sqlite3.Row
c=baza.cursor()

c.execute('DROP TABLE IF EXISTS pytania')
c.execute("CREATE TABLE pytania(id integer primary key,trescPytania varchar(100))")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Płeć')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Wiek')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Waga')")
c.execute("INSERT INTO pytania(trescPytania) VALUES('Wzrost')")
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
c.execute("CREATE TABLE odpowiedzi(id integer primary key, idPytania integer, trescOdpowiedzi varchar(30) )")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(1,'Kobieta')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(1,'Mężczyzna')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(5,'Bardzo dobrze')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(5,'Poprawnie')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(5,'Mogłoby być lepiej')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(5,'Źle')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(6,'Codziennie')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(6,'3-5 razy w tygodniu')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(6,'2-3 razy w tygodniu')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(6,'Sporadycznie')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(6,'Nigdy, nie mam czasu na trening')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(7,'Zdecydowanie tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(7,'Raczej tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(7,'Raczej nie')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(7,'Zdecydowanie nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(8,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(8,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(9,'Zdecydowanie nie')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(9,'Piję tylko w wyjątkowych sytuacjach')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(9,'Piję zawsze kiedy mam okazję')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(9,'Piję nałogowo')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(10,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(10,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(11,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(11,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(12,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(12,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(13,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(13,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(14,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(14,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(15,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(15,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(16,'Tak')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(16,'Nie')")

c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(17,'podstawowe nieukończone i bez wykształcenia')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(17,'podstawowe ukończone')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(17,'zasadnicze zawodowe')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(17,'średnie zawodowe')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(17,'średnie ogólnokształcące')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(17,'policealne')")
c.execute("INSERT INTO odpowiedzi(idPytania,trescOdpowiedzi) VALUES(17,'wyższe')")


baza.commit()
c.close()
baza.close()

