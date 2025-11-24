from lista_encadeada import ListaEncadeada

class TabelaHash:
    def __init__(self):
        self.M = 11
        self.tabela = [ListaEncadeada() for _ in range(self.M)]

    def funcao_hash(self, chave):
        return chave % self.M

    def inserir(self, aluno):
        endereco = self.funcao_hash(aluno.matricula)
        return self.tabela[endereco].inserir(aluno)

    def buscar(self, matricula):
        endereco = self.funcao_hash(matricula)
        return self.tabela[endereco].buscar(matricula)

    def remover(self, matricula):
        endereco = self.funcao_hash(matricula)
        return self.tabela[endereco].remover(matricula)

    def exibir_tabela(self):
        print("\n===== TABELA HASH =====")
        for i in range(self.M):
            print(f"[{i}] -> ", end="")
            self.tabela[i].exibir()