from no import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, aluno):
        if self.buscar(aluno.matricula) is not None:
            return False

        novo = No(aluno)

        if self.inicio is None:
            self.inicio = novo
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = novo

        return True

    def buscar(self, matricula):
        aux = self.inicio
        while aux is not None:
            if aux.aluno.matricula == matricula:
                return aux.aluno
            aux = aux.proximo
        return None

    def remover(self, matricula):
        if self.inicio is None:
            return False

        if self.inicio.aluno.matricula == matricula:
            self.inicio = self.inicio.proximo
            return True

        anterior = None
        atual = self.inicio

        while atual is not None and atual.aluno.matricula != matricula:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return False

        anterior.proximo = atual.proximo
        return True

    def exibir(self):
        aux = self.inicio
        while aux is not None:
            print(aux.aluno, end=" -> ")
            aux = aux.proximo
        print("None")