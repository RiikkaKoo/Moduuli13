# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
# aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    jatka = True
    jakaja = 1
    while jatka == True:
        jakaja += 1
        if luku % jakaja == 0 and jakaja < luku:
            tulos = False
            jatka = False
        elif luku % jakaja == 0 and jakaja == luku:
            tulos = True
            jatka = False

    vastaus = {
        'Number' : luku,
        'isPrime' : tulos
    }

    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)