from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username[0].isupper() and any(char.isalpha() and char.isdigit() for char in password):
        return redirect(url_for('login_success'))
    else:
        return redirect(url_for('index'))

@app.route('/login_success')
def login_success():
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
