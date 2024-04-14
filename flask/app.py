from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    """Renderiza a página de login.

    Returns:
        str: O conteúdo HTML da página de login.
    """
    return render_template('login.html')

# Rota para efetuar o login
@app.route('/login', methods=['POST'])
def login():
    """Processa a tentativa de login.

    Obtém as credenciais do formulário de login.
    Verifica as credenciais e redireciona para a página de sucesso se forem corretas.

    Returns:
        str: Redireciona para a página de sucesso ou exibe uma mensagem de falha no login.
    """
    username = request.form['username']
    password = request.form['password']
    
    # Verifica as credenciais
    if username == "admin@example.com" and password == "secret":
        return redirect(url_for('success'))
    else:
        return "Falha no login!"

# Rota para a página de sucesso
@app.route('/success')
def success():
    """Página de sucesso após o login.

    Returns:
        str: O conteúdo HTML da página de sucesso.
    """
    return "Login bem-sucedido!"

if __name__ == '__main__':
    app.run(debug=True)
