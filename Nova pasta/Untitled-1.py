import re

nome_arquivo = "a.txt"
def abre_arquivo(nomeArquivo):
    dados = open(nomeArquivo)
    for linha in dados:
        print(linha)
        linha = linha.replace(" ","")
        elementos = linha.split("=")
        le = elementos[0]
        ld = elementos[1].rstrip()
        termos = re.split("-|\+",le)
        print(termos)

abre_arquivo(nome_arquivo)
#ax+by=c
# y=c/b

# def eixo_Y():
#     y = c/b
#     print(y)

# def eixo_x():
#     x = c/a
#     print(x)


# x=2
# y=3
# func = (a*x)+(b*y) <= c

# print(func)
# eixo_Y()
# eixo_x()
