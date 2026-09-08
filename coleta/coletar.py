from .camara import deputados
from .camara import proposicoes
from .camara import votacoes
# from camara import despesas


def coletar():
    deputados.coletar()
    proposicoes.coletar()
    votacoes.coletar()
    # despesas.coletar()


if __name__ == "__main__":
    coletar()