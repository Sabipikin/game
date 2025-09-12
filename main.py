from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    message = ""
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1
            if guess < session['number']:
                message = "Too low! Try a higher number."
            elif guess > session['number']:
                message = "Too high! Try a lower number."
            else:
                message = f"Congratulations! You guessed the number {session['number']} in {session['attempts']} attempts."
                session.pop('number')  # Reset for new game
                session.pop('attempts')
        except ValueError:
            message = "Please enter a valid number."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)