from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Connexion MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/don', methods=['GET', 'POST'])
def don():
    if request.method == 'POST':
        nom = request.form['nom']
        montant = request.form['montant']
        moyen = request.form['moyen']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dons (nom, montant, moyen) VALUES (%s, %s, %s)", (nom, montant, moyen))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('merci'))

    return render_template('don.html')

@app.route('/merci')
def merci():
    return render_template('merci.html')

if __name__ == '__main__':
    app.run(debug=True)
