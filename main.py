from controllers.aluno_controller import *
from views.menu_view import *

while True:

    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome: ")

        while validar_nome(nome) == False:
            print("Nome inválido.")
            nome = input("Nome: ")

        idade = int(input("Idade: "))
        turma = input("Turma: ")

        frequencia = float(
            input("Frequência (%): ")
        )

        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        aluno = {
            "nome": nome,
            "idade": idade,
            "turma": turma,
            "frequencia": frequencia,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3
        }

        salvar_aluno(aluno)

        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":

        nome = input(
            "Nome do aluno para alterar notas: "
        )

        atualizar_notas(nome)

    elif opcao == "3":

        listar_alunos()

    elif opcao == "4":

        nome = input("Nome do aluno: ")

        aluno = buscar_aluno(nome)

        if aluno:

            media = calcular_media(
                aluno["nota1"],
                aluno["nota2"],
                aluno["nota3"]
            )

            situacao = verificar_situacao(
                media,
                aluno["frequencia"]
            )

            print("\nNome:", aluno["nome"])
            print("Turma:", aluno["turma"])
            print("Média:", round(media, 2))
            print("Situação:", situacao)

        else:
            print("Aluno não encontrado.")

    elif opcao == "5":

        print("\n=== APROVADOS ===")
        listar_aprovados()

    elif opcao == "6":

        print("\n=== REPROVADOS / RECUPERAÇÃO ===")
        listar_reprovados()

    elif opcao == "0":

        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")