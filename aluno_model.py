def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def verificar_situacao(media, frequencia):

    if frequencia < 75:
        return "REPROVADO POR FALTA"

    if media >= 7:
        return "APROVADO"

    elif media >= 3:
        return "RECUPERACAO"

    else:
        return "REPROVADO"