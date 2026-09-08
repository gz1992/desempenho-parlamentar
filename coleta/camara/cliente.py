import httpx


class ClienteCamara:
    URL_BASE = "https://dadosabertos.camara.leg.br/api/v2"
    URL_ARQUIVOS = "https://dadosabertos.camara.leg.br/arquivos"

    def __init__(self):
        self.cliente = httpx.Client(
            timeout=60.0,
            headers={
                "Accept": "application/json",
            },
        )

    def buscar(self, caminho, parametros=None):
        resposta = self.cliente.get(
            f"{self.URL_BASE}/{caminho}",
            params=parametros,
        )

        resposta.raise_for_status()

        return resposta.json()

    def baixar_json(self, caminho):
        resposta = self.cliente.get(caminho)

        resposta.raise_for_status()

        return resposta.json()

    def fechar(self):
        self.cliente.close()