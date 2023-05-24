import requests
import os

cep = input("Informe um CEP:")
url = "https://brasilapi.com.br/api/cep/v1/" + cep

response = requests.get(url)

if response.status_code == 200:

    data = response.json()


    print("CEP:", data('cep'))
    print("Estado:", data('state'))
    print("Cidade:", data('city'))
    print("Vizinhança:", data('neighborhood'))
    print("Rua:", data('street'))
    print("Serviço:", data('service'))

else:
    # Imprime o código de erro HTTP
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))


os.system("PAUSE")