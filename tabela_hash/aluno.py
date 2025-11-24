class Aluno:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"[Matricula: {self.matricula}, Nome: {self.nome}, Idade: {self.idade}]"