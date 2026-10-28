
import sys
import requests

url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"

try: 
    resposta = requests.get(url,timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()

    bid = float(dados["BTCBRL"]["bid"])
    high = float(dados["BTCBRL"]["high"])
    low = float(dados["BTCBRL"]["low"])
    varBid = float(dados["BTCBRL"]["varBid"])
    create_date = (dados["BTCBRL"]["create_date"])
    preco_referencia = bid - varBid
    percentual_variacao = (varBid / preco_referencia) * 100
except (requests.exceptions.RequestException, ValueError, KeyError):
    print("Sem conexão ou API indisponível.\nTente mais tarde.")
    sys.exit(1)

def formatar_real(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")

    return texto

print("="*50)
print("ANÁLISE DE MERCADO — BTC/BRL".center(50))
print("="*50)

print(f"Cotação atual: R$ {formatar_real(bid)}".center(50))
print(f"Máxima do período:  R$ {formatar_real(high)}".center(50))
print(f"Mínima do período: R$ {formatar_real(low)}".center(50))
print(f"Preço de referência: R$ {formatar_real(preco_referencia)}".center(50))
print(f"Variação em reais: R$ {formatar_real(varBid)}".center(50))
print(f"Variação percentual: {formatar_real(percentual_variacao)}%".center(50))
print()
print(f"Atualização: {(create_date)}".center(50))

print("="*50)
print("Dados obtidos via API".center(50))
print("="*50)
input("\n\n\n\nPressione ENTER para sair")