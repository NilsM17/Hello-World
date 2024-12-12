import random
from flask import Flask, request, render_template_string, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

@app.route('/', methods=['GET', 'POST'])
def zahlrate_spiel():
    if 'zahl' not in session:
        session['zahl'] = random.randint(1, 100)
        session['versuche'] = 10
        session['last_eingabe'] = -1

    zahl = session['zahl']
    versuche = session['versuche']
    last_eingabe = session['last_eingabe']
    message = "Bitte Zahl zwischen 1 und 100 eingeben:"

    if request.method == 'POST':
        eingabe = int(request.form['eingabe'])
        if eingabe == last_eingabe:
            message = "Bist du Dumm oder so?"
        elif eingabe < zahl:
            message = "Zu niedrig"
        else:
            message = "Zu hoch"
        session['last_eingabe'] = eingabe
        session['versuche'] -= 1
        if eingabe == zahl:
            message = f"Richtig geraten! Die Zahl war: {zahl}. Das Spiel wird neu gestartet."
            session.pop('zahl', None)
            session.pop('versuche', None)
            session.pop('last_eingabe', None)
        elif session['versuche'] == 0:
            message = "Leider verloren! Das Spiel wird neu gestartet."
            session.pop('zahl', None)
            session.pop('versuche', None)
            session.pop('last_eingabe', None)

    return render_template_string('''
        <html>
            <head>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        font-family: Arial, sans-serif;
                        background-color: #f0f0f0;
                        margin: 0;
                    }
                    .container {
                        text-align: center;
                        background: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                    input[type="number"] {
                        padding: 10px;
                        margin: 10px 0;
                        width: calc(100% - 22px);
                        box-sizing: border-box;
                    }
                    input[type="submit"] {
                        padding: 10px 20px;
                        background-color: #007BFF;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    input[type="submit"]:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Zahlrate-Spiel</h1>
                    <p>{{ message }}</p>
                    <form method="post">
                        <input type="number" name="eingabe" required>
                        <input type="submit" value="Rate">
                    </form>
                </div>
            </body>
        </html>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)
