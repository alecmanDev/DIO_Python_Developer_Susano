# Podemos combinar parâmetros obrigatórios com args e kwargs
# *args == lista
# **kwargs == dicionário

def  exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso} \n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Segunda-feira, 03 de março de 2024",
    "Quando me tratas mal e, desprezado,",
    "Sinto que o meu valor vês com desdém,",
    "Lutando contra mim, fico a teu lado",
    "E, inda perjuro, provo que és um bem.",
    "\n"
    "Conhecendo melhor meus próprios erros,",
    "A te apoiar te ponho a par da história",
    "De ocultas faltas, onde estou enfermo;",
    "Então, ao me perder, tens toda a glória.",
    "\n"
    "Mas lucro também tiro desse ofício:",
    "Curvando sobre ti amor tamanho,",
    "Mal que me faço me traz benefício,",
    "\n"
    "Pois o que ganhas duas vezes ganho.",
    "Assim é o meu amor e a ti o reporto:",
    "Por ti todas as culpas eu suporto.",
    autor="William Shakespeare",
    ano=1616,
)