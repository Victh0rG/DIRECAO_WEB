from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')  # 'templates'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # credenciais
    if username == "admin@example.com" and password == "secret":
        return redirect(url_for('success'))
    else:
        return "Falha no login!"

@app.route('/success')
def success():
    return "Login bem-sucedido!"

if __name__ == '__main__':
    app.run(debug=True)