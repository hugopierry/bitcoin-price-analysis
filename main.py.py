from time import sleep
import requests
import pandas as pd

url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"

# Exemplo de resposta da API para consulta dos campos disponíveis.

# dados_api = {
#   "BTCBRL": {
#     "code": "BTC",
#     "codein": "BRL",
#     "name": "Bitcoin/Real Brasileiro",
#     "high": "437644",
#     "low": "397171",
#     "varBid": "23860",
#     "pctChange": "5.883",
#     "bid": "429418",
#     "ask": "429419",
#     "timestamp": "1792984472",
#     "create_date": "2026-10-26 00:14:32"
#   }
# }
resposta = requests.get(url)
dados = resposta.json()

bid = float(dados["BTCBRL"]["bid"])
high = float(dados["BTCBRL"]["high"])
low = float(dados["BTCBRL"]["low"])
varBid = float(dados["BTCBRL"]["varBid"])
pctChange = float(dados["BTCBRL"]["pctChange"])


def formatar_real(valor):
    
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")

    return texto

print("="*50)
print("ANÁLISE DE MERCADO — BTC/BRL".center(50))
print("="*50)
sleep(2)
print(f"Cotação atual: R$ {formatar_real(bid)}".center(50))
print(f"Máxima do período:  R$ {formatar_real(high)}".center(50))
print(f"Mínima do período: R$ {formatar_real(low)}".center(50))
print(f"Variação em reais: R$ {formatar_real(varBid)}".center(50))
print(f"Variação percentual: {formatar_real(pctChange)}%".center(50))

print("="*50)
print("Dados obtidos via API".center(50))
print("="*50)
input("\n\n\n\nPressione ENTER para sair")
