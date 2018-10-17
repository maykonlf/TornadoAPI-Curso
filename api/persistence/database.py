import sqlite3

__conn = None


def dict_factory(cursor, row):
    d = {}
    for index, collumn in enumerate(cursor.description):
        d[collumn[0]] = row[index]
    return d


def get_conn() -> sqlite3.Connection:
    global __conn
    if __conn is None:
        __conn = sqlite3.connect("database.sqlite")
        __conn.row_factory = dict_factory
    return __conn


def prepare_database():
    conn = get_conn()
    conn.execute('''
            CREATE TABLE IF NOT EXISTS bovinos (
              id INTEGER PRIMARY KEY,
              nome VARCHAR(50) NOT NULL,
              peso DOUBLE NOT NULL,
              nascimento VARCHAR(10),
              disponivelVenda BIT,
              idRaca INTEGER REFERENCES racas(id)
            );
        ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS racas (
            id INTEGER PRIMARY KEY,
            descricao VARCHAR(20) NOT NULL
        )
    ''')

    conn.execute("INSERT INTO racas(id, descricao) SELECT 1, 'nelore' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 1)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 2, 'senepol' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 2)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 3, 'black angus' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 3)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 4, 'red angus' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 4)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 5, 'tabapuã' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 5)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 6, 'holandês' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 6)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 7, 'girolando' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 7)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 8, 'gir' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 8)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 9, 'bonsmara' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 9)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 10, 'guzerá' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 10)")
    conn.execute("INSERT INTO racas(id, descricao) SELECT 11, 'wagyu' WHERE NOT EXISTS(SELECT 1 FROM racas WHERE id = 11)")

    conn.commit()

def connect():
    prepare_database()


def adicionar_bovino(item: dict):
    conn = get_conn()
    conn.execute("INSERT INTO bovinos (nome, peso, nascimento, disponivelVenda, idRaca) values (?,?,?,?,?)",
                 (item.get("nome"), item.get("peso"), item.get("nascimento"), item.get("disponivelVenda", False), item.get("idRaca")))
    conn.commit()


def listar_bovinos():
    bovinos = []
    for row in get_conn().execute("SELECT * FROM bovinos"):
        if row.get("disponivelVenda"):
            row.update(disponivelVenda=True)
        else:
            row.update(disponivelVenda=False)
        bovinos.append(row)
    return bovinos


def atualizar_bovino(id, item: dict):
    conn = get_conn()
    conn.execute("UPDATE bovinos SET nome = ?, peso = ?, nascimento = ?, disponivelVenda = ? WHERE id = ?",
                 (item.get("nome"), item.get("peso"), item.get("nascimento"), item.get("disponivelVenda", False), item.get("idRaca"), id))
    conn.commit()


def excluir_bovino(id):
    conn = get_conn()
    conn.execute("DELETE FROM bovinos WHERE id = ?", (id,))
    conn.commit()


def consultar_bovino(id):
    bovinos = []
    for row in get_conn().execute("SELECT * FROM bovinos WHERE id = ?", (id,)):
        bovinos.append(row)
    return bovinos[0] if len(bovinos) > 0 else None


def listar_racas():
    racas = []
    for row in get_conn().execute("SELECT * FROM racas"):
        racas.append(row)
    return racas
