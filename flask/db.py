import sqlite3
import click
from flask import current_app, g

def get_db():
    """Obtém uma conexão com o banco de dados.

    Verifica se já existe uma conexão no contexto do aplicativo Flask (g).
    Se não houver, cria uma nova conexão com o banco de dados definido na configuração.
    Configura a fábrica de linhas para retornar linhas como dicionários.
    
    Returns:
        sqlite3.Connection: Conexão com o banco de dados.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """Fecha a conexão com o banco de dados.

    Fecha a conexão com o banco de dados se estiver presente no contexto do aplicativo Flask (g).

    Args:
        e: Exception, opcional, utilizado para receber exceções do Flask.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """Inicializa o banco de dados.

    Obtém uma conexão com o banco de dados e executa o script SQL de inicialização
    para criar as tabelas necessárias.

    Raises:
        sqlite3.Error: Se ocorrer um erro durante a execução do script SQL.
    """
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Comando CLI para inicializar o banco de dados.

    Chama a função init_db para inicializar o banco de dados
    e imprime uma mensagem de confirmação.

    Usage:
        flask init-db
    """
    init_db()
    click.echo('Inicializando o database.')

def init_app(app):
    """Inicializa o aplicativo Flask.

    Adiciona funções close_db e comandos CLI para o aplicativo.

    Args:
        app: Flask, o aplicativo Flask a ser inicializado.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
