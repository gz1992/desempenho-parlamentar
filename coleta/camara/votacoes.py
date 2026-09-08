import json
from datetime import date

from .cliente import ClienteCamara


ANO_INICIAL = 2022


def pegar_votacoes(cliente: ClienteCamara, ano):
    url = (
        "https://dadosabertos.camara.leg.br/"
        f"arquivos/votacoes/json/votacoes-{ano}.json"
    )

    dados = cliente.baixar_json(url)

    return dados["dados"]


def pegar_votos(cliente: ClienteCamara, ano):
    url = (
        "https://dadosabertos.camara.leg.br/"
        f"arquivos/votacoesVotos/json/votacoesVotos-{ano}.json"
    )

    dados = cliente.baixar_json(url)

    return dados["dados"]


def pegar_historico(
    cliente: ClienteCamara,
    ano_inicial=ANO_INICIAL,
    ano_final=None,
):
    if ano_final is None:
        ano_final = date.today().year

    votacoes = []
    votos = []

    for ano in range(ano_inicial, ano_final + 1):
        print(f"Coletando votações de {ano}...")

        votacoes_ano = pegar_votacoes(cliente, ano)
        votos_ano = pegar_votos(cliente, ano)

        votacoes.extend(votacoes_ano)
        votos.extend(votos_ano)

        print(f"  {len(votacoes_ano)} votações")
        print(f"  {len(votos_ano)} votos")

    return {
        "votacoes": votacoes,
        "votos": votos,
    }


def coletar():
    cliente = ClienteCamara()

    try:
        return pegar_historico(cliente)

    finally:
        cliente.fechar()


if __name__ == "__main__":
    dados = coletar()

    print(
        f"Total de votações: "
        f"{len(dados['votacoes'])}"
    )

    print(
        f"Total de votos: "
        f"{len(dados['votos'])}"
    )

    print("\n=== VOTAÇÃO ===")
    print(
        json.dumps(
            dados["votacoes"][0],
            indent=2,
            ensure_ascii=False,
        )
    )

    print("\n=== VOTO ===")
    print(
        json.dumps(
            dados["votos"][0],
            indent=2,
            ensure_ascii=False,
        )
    )