import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cur = conexao.cursor()
cur.row_factory = sqlite3.Row

def criar_tabela(cur):
    cur.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCAR(100), email VARCHAR(150))'
    )

def inserir_registro(conexao, cur, nome, email):
    data = (nome, email)
    cur.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
    conexao.commit()

def atualizar_registro(conexao, cur, nome, email, id):
    data = (nome, email, id)
    cur.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', data)
    conexao.commit()

#atualizar_registro(conexao, cur, 'Leonardo Portugal', "leo@gmail.com", 1)

def excluir_registro(conexao, cur, id):
    data = (id,)
    cur.execute('DELETE FROM clientes WHERE id = ?', data)
    conexao.commit()

#excluir_registro(conexao, cur, 2)

def inserir_muitos(conexao, cur, dados):
    cur.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', dados)
    conexao.commit()

#dados = [
    #('Nicole', 'nicks@gmail.com'),
    #('Ana', 'ana@gmail.com'),
    #('João', 'joao@gmail.com'),
    #('Claúdio', 'claudio@gmail.com')
#]

#inserir_muitos(conexao, cur, dados) 

def recuperar_cliente(cur, id):
    cur.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    return cur.fetchone()

def listar_clientes(cur):
    return cur.execute('SELECT * FROM clientes;')

clientes = listar_clientes(cur)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cur, 1)
print(dict(cliente))



