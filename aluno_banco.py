import pymysql.cursors
from aluno import Aluno

class AlunoBanco:
    def __init__(self, host: str, username: str, db: str, password: str):
        self.conexao = self.criarConexao(host, username, db, password)

        self.cursor = self.conexao.cursor()

    def criarConexao(self, host: str, username: str, db: str, password: str):
        try:
            conn = pymysql.connect(host=host,
                                   user=username,
                                   db=db,
                                   password=password,
                                   cursorclass=pymysql.cursors.DictCursor)
            return conn

        except Exception as error:
            print(f"Erro ao conectar ao Banco de Dados! Erro: {error}")

    def insert(self, aluno: Aluno):
        try:
            sql = "Insert Into alunos (matricula, nome, idade, curso, nota) Values (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (aluno.matricula, aluno.nome,
                                            aluno.idade, aluno.curso, aluno.nota))
            self.conexao.commit()
            print("Aluno cadastradado com sucesso!")
        except Exception as error:
            print(f"Erro ao inserir um Aluno(a)! {error}")

    def update(self, aluno: Aluno):
        try:
            sql = "Update alunos Set nome = %s, idade = %s, curso = %s, nota = %s Where matricula = %s"
            self.cursor.execute(sql, (aluno.nome,
                                            aluno.idade, aluno.curso, aluno.nota, aluno.matricula))
            self.conexao.commit()
            print('Dados alterados!')
        except Exception as error:
            print(f"Erro ao editar Dados! Erro: {error}")

    def delete(self, matricula: int):
        try:
            sql = "Delete from alunos Where matricula = %s"
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
            print("Dados removidos com sucesso!")
        except Exception as error:
            print(f"Erro ao deletar! Erro: {error}")

    def select(self):
        try:
            sql = "Select * From alunos"
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f"Erro ao listar! Erro: {error}")


if __name__ == "__main__":
    a = AlunoBanco('localhost', 'root', 'escola', '')
    aluno1 = Aluno('Jonas', 19, 'Java', 8.7)
    aluno2 = Aluno('Isaac', 23, 'Python', 9.0)

    a.insert(aluno1)
    a.insert(aluno2)
    print(a.select())
    aluno1.nome = 'Jonas Lopes'
    a.update(aluno1)
    print(a.select())
    a.delete(aluno2. matricula)
    print(a.select())
