from .cliente import ClienteCamara

class Deputados:

    def pegar_todos(cliente: ClienteCamara):
        deputados = []

        parametros = {
            "itens": 100,
            "pagina": 1,
            "ordem": "ASC",
            "ordenarPor": "nome",
        }

        while True:
            resposta = cliente.buscar(
                "deputados",
                parametros,
            )

            deputados.extend(resposta["dados"])

            proxima_pagina = next(
                (
                    link["href"]
                    for link in resposta["links"]
                    if link["rel"] == "next"
                ),
                None,
            )

            if not proxima_pagina:
                break

            parametros["pagina"] += 1

        return deputados


def coletar():
    cliente = ClienteCamara()

    try:
        deputados = Deputados.pegar_todos(cliente)

        return deputados

    finally:
        cliente.fechar()


if __name__ == "__main__":
    deputados = coletar()

    print("\n=== DEPUTADO ===")
    print(deputados[0])