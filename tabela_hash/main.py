from tabela_hash import TabelaHash
from aluno import Aluno

def main():
    tabela = TabelaHash()

    while True:
        print("\n===== MENU =====")
        print("1 - Inserir Aluno")
        print("2 - Buscar Aluno")
        print("3 - Remover Aluno")
        print("4 - Exibir Tabela Hash")
        print("5 - Encerrar Sistema")

        opcao = input("Escolha: ")

        if opcao == "1":
            matricula = int(input("Matrícula: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))

            aluno = Aluno(matricula, nome, idade)

            if tabela.inserir(aluno):
                print("Aluno inserido com sucesso!")
            else:
                print("ERRO: Matrícula já cadastrada!")

        elif opcao == "2":
            matricula = int(input("Digite a matrícula para buscar: "))
            aluno = tabela.buscar(matricula)
            if aluno:
                print("Aluno encontrado:", aluno)
            else:
                print("Aluno não encontrado!")

        elif opcao == "3":
            matricula = int(input("Digite a matrícula para remover: "))
            if tabela.remover(matricula):
                print("Aluno removido!")
            else:
                print("Aluno não encontrado!")

        elif opcao == "4":
            tabela.exibir_tabela()

        elif opcao == "5":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()