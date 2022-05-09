from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

db = {
    "Pavel": "Pujdes na drink Pavle?",
    "Jiri": "Budes delat ten Tik Tok?"
}

@app.route('/informace')
def info():
    return '<p style="color: red">Pro vice informaci kontaktujte zakaznickou podporu.</p>'

@app.route('/')
def index():
    return render_template('index.html', databaze=db)

@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    if request.method == "GET":
        return render_template('kontakt.html')
    elif request.method == "POST":
        jmeno = request.form['jmeno']
        dotaz = request.form['dotaz']
        db[jmeno] = dotaz
        return render_template('kontakt.html', odpoved="Dotaz byl uspesne zaslan.")

if __name__ == "__main__":
    app.run(debug=True, port=8080)

