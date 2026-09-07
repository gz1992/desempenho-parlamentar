import httpx


class ClienteCamara:
    URL_BASE = "https://dadosabertos.camara.leg.br/api/v2"

    def __init__(self):
        self.cliente = httpx.Client(
            base_url=self.URL_BASE,
            timeout=30.0,
            headers={
                "Accept": "application/json",
            },
        )

    def buscar(self, caminho, parametros=None):
        resposta = self.cliente.get(
            caminho,
            params=parametros,
        )

        resposta.raise_for_status()

        return resposta.json()

    def fechar(self):
        self.cliente.close()