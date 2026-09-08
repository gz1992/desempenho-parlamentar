from datetime import date

from .cliente import ClienteCamara


URL_ARQUIVO = (
    "https://dadosabertos.camara.leg.br/"
    "arquivos/proposicoes/json/proposicoes-{ano}.json"
)

ANO_INICIAL = 2022


def pegar_arquivo(cliente: ClienteCamara, ano):
    url = URL_ARQUIVO.format(ano=ano)

    dados = cliente.baixar_json(url)

    if isinstance(dados, dict):
        return dados["dados"]

    return dados


def pegar_historico(
    cliente: ClienteCamara,
    ano_inicial=ANO_INICIAL,
    ano_final=None,
):
    if ano_final is None:
        ano_final = date.today().year

    proposicoes = []

    for ano in range(ano_inicial, ano_final + 1):
        print(f"Coletando proposições de {ano}...")

        proposicoes_ano = pegar_arquivo(cliente, ano)

        proposicoes.extend(proposicoes_ano)

        print(
            f"  {len(proposicoes_ano)} proposições encontradas"
        )

    return proposicoes


def coletar():
    cliente = ClienteCamara()

    try:
        proposicoes = pegar_historico(cliente)

        print(
            f"Total de proposições coletadas: "
            f"{len(proposicoes)}"
        )

        return proposicoes

    finally:
        cliente.fechar()


if __name__ == "__main__":
    proposicoes = coletar()

    print("\n=== PROPOSIÇÃO ===")
    print(proposicoes[0])