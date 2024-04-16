import requests

class Consulta_Utils:
    def __init__():
        pass
    def consulta_ddd(ddd: int) -> str:
        url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            state = data['state']
            return state
        else:
            return "Não foi possível consultar o DDD."

