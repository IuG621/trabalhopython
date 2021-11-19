import sqlite3
conn = sqlite3.connect("trabalho/escola.db")


def criar_tabela():
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS escola(
                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        av1 FLOAT,
                        av2 FLOAT,
                        av3 FLOAT,
                        avd FLOAT,
                        avds FLOAT)''')
    except Exception as e:
        print("Erro na criação da tabela: ", e)

def add_aluno(nome, av1, av2, av3, avd, avds):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO escola (nome, av1, av2, av3, avd, avds) VALUES (?, ?, ?, ?, ?, ? )',(nome, av1, av2, av3, avd, avds))
        conn.commit()
    except sqlite3.Error as e:
        print("Erro ao inserir o aluno: ", e)
    finally:
        cursor.close()

def get_aluno():
    try:
        return conn.execute('SELECT id_aluno, nome, av1, av2, av3, avd, avds FROM escola')
    except sqlite3.Error as e:
        print("Erro ao buscar o aluno: ", e)

def excluir_aluno(id_aluno):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM escola WHERE id_aluno = ?',(id_aluno, ))
        conn.commit()
        conn.execute('VACUUM')
    except sqlite3.Error as e:
        print('Erro ao excluir aluno: ', e)
    finally:
        cursor.close()

def alterar_aluno(id_aluno, nome):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE escola set nome = ? WHERE id_aluno = ?'''
        dado = (nome, id_aluno)
        cursor.execute(update_query, dado)
        conn.commit()
        print('Atualizado com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao alterar aluno: ', e)
    finally:
        cursor.close()
