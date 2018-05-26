from flask import Flask, request, jsonify, g
from flask import render_template
import sqlite3

DATABASE = 'baza.db'
aplikacja=Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@aplikacja.route("/")
def stronaStartowa():
    with aplikacja.app_context():
        db = get_db()
        c = db.cursor()
        c.execute("SELECT * FROM pytania")
        wynik = c.fetchall()

        pytania = []
        for x in wynik:
            pytanie = dict(x)
            c.execute("SELECT * FROM odpowiedzi WHERE idPytania=" + str(pytanie['id']))
            odpowwiedzi = c.fetchall()
            doDodania = {'ans': pytanie['trescPytania'], 'odp': []}
            for o in odpowwiedzi:
                odpoSl = dict(o)
                doDodania['odp'].append(odpoSl['trescOdpowiedzi'])
            pytania.append(doDodania)


        return render_template('ankietaStrona.html',pytania=pytania)

@aplikacja.route("/wyslijDane", methods=['POST'])
def wyslijDane():
    r = request.json

    

    zwrotka = {'result': True}
    return jsonify(zwrotka)

if __name__ == '__main__':
    aplikacja.run(debug=True)