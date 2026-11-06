from models.aluno_model import *
from utils.validacoes import *

ARQUIVO = "database/alunos.txt"


def salvar_aluno(aluno):

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:

        linha = (
            f"{aluno['nome']};"
            f"{aluno['idade']};"
            f"{aluno['turma']};"
            f"{aluno['frequencia']};"
            f"{aluno['nota1']};"
            f"{aluno['nota2']};"
            f"{aluno['nota3']}\n"
        )

        arquivo.write(linha)


def carregar_alunos():

    alunos = []

    try:

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                aluno = {
                    "nome": dados[0],
                    "idade": int(dados[1]),
                    "turma": dados[2],
                    "frequencia": float(dados[3]),
                    "nota1": float(dados[4]),
                    "nota2": float(dados[5]),
                    "nota3": float(dados[6])
                }

                alunos.append(aluno)

    except FileNotFoundError:
        pass

    return alunos


def listar_alunos():

    alunos = carregar_alunos()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:

        media = calcular_media(
            aluno["nota1"],
            aluno["nota2"],
            aluno["nota3"]
        )

        situacao = verificar_situacao(
            media,
            aluno["frequencia"]
        )

        print("\n----------------------")
        print("Nome:", aluno["nome"])
        print("Turma:", aluno["turma"])
        print("Frequência:", aluno["frequencia"])
        print("Média:", round(media, 2))
        print("Situação:", situacao)


def buscar_aluno(nome):

    alunos = carregar_alunos()

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():
            return aluno

    return None


def listar_aprovados():

    alunos = carregar_alunos()

    for aluno in alunos:

        media = calcular_media(
            aluno["nota1"],
            aluno["nota2"],
            aluno["nota3"]
        )

        situacao = verificar_situacao(
            media,
            aluno["frequencia"]
        )

        if situacao == "APROVADO":
            print(aluno["nome"])


def listar_reprovados():

    alunos = carregar_alunos()

    for aluno in alunos:

        media = calcular_media(
            aluno["nota1"],
            aluno["nota2"],
            aluno["nota3"]
        )

        situacao = verificar_situacao(
            media,
            aluno["frequencia"]
        )

        if situacao != "APROVADO":
            print(aluno["nome"])


def atualizar_notas(nome):

    alunos = carregar_alunos()

    encontrado = False

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            aluno["nota1"] = float(input("Nova nota 1: "))
            aluno["nota2"] = float(input("Nova nota 2: "))
            aluno["nota3"] = float(input("Nova nota 3: "))

            encontrado = True

    if not encontrado:
        print("Aluno não encontrado.")
        return

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        for aluno in alunos:

            linha = (
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['turma']};"
                f"{aluno['frequencia']};"
                f"{aluno['nota1']};"
                f"{aluno['nota2']};"
                f"{aluno['nota3']}\n"
            )

            arquivo.write(linha)

    print("Notas atualizadas.")