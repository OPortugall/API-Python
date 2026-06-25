import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cur = conexao.cursor()
cur.row_factory = sqlite3.Row

try:
    cur.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('Teste 1', 'teste1@gmail.com'))
    cur.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)', (2, 'Teste 2', 'teste2@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f'Ops! um erro ocorreu! {exc}')
    conexao.rollback()
