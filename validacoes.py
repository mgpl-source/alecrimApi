def validar_nome(nome):

    nome = nome.replace(" ", "")

    return nome.isalpha()


def validar_nota(nota):

    return 0 <= nota <= 10


def validar_frequencia(freq):

    return 0 <= freq <= 100