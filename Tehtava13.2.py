# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja
# kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def kentän_tiedot(icao):
    sql = f'SELECT ident, name, municipality FROM airport WHERE ident = "{icao}";'
    print(sql)
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    airport_data = kursori.fetchall()
    tiedot = airport_data[0]  # Tässä vaiheessa järjestys on vielä: ICAO - name - municipality,
                                # mutta netissä näytettävä tieto on järjestyksessä:
                                # ICAO - municipality - name (aakkosjärjestyksessä?). Miksi? Voiko sen muuttaa?
    return tiedot


yhteys = mysql.connector.connect(
    host='127.0.0.1',  # host='localhost'
    port=3306,
    database='flight_game',
    user='käyttäjä',
    password='salasana',
    autocommit=True
)

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)