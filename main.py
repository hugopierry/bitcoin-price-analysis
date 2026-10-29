import sys
import requests
import os


url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
os.system("")


CORES = {
    # cores normais
    "preto": "\033[30m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",
    # cores claras
    "cinza": "\033[90m",
    "vermelho_claro": "\033[91m",
    "verde_claro": "\033[92m",
    "amarelo_claro": "\033[93m",
    "azul_claro": "\033[94m",
    "magenta_claro": "\033[95m",
    "ciano_claro": "\033[96m",
    # estilos
    "negrito": "\033[1m",
    "sublinhado": "\033[4m",
    # volta ao normal
    "reset": "\033[0m",
}

LARGURA = 50
R = CORES["reset"]

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
def linha_valor(rotulo, valor, cor):
    espaco = (LARGURA - len(rotulo + valor)) //2
    print(" " * espaco + rotulo + cor + valor + R)

print("╔" + "═"*LARGURA + "╗")
print(CORES["negrito"] + CORES['azul'] + "ANÁLISE DE MERCADO — BTC/BRL".center(LARGURA) + R)
print("╚" + "═" * LARGURA + "╝")

linha_valor( "Cotação atual: ", f"R$ {formatar_real(bid)}", CORES["negrito"] + CORES["ciano"]  )
# Se o valor estiver positivo, o resultado fica verde
linha_valor("Máxima do período: ",f"R$ {formatar_real(high)}",CORES["verde"])
linha_valor("Mínima de período: ", f"R$ {formatar_real(low)}", CORES["vermelho"])
linha_valor("Preço de referência: ",f"R$ {formatar_real(preco_referencia)}", CORES["cinza"])

# condições para melhor visualização
cor_var = CORES["verde"] if varBid >= 0 else CORES["vermelho"]
linha_valor("Variação em reais: ", f"R$ {formatar_real(varBid)}", cor_var)
linha_valor("Variação percentual: ", f"{formatar_real(percentual_variacao)}%", cor_var)

print()

print(f"Atualização: {create_date}".center(LARGURA))


print("Dados obtidos via API".center(LARGURA))

print()
print()
print()
print()
print()
input("Pressione ENTER para sair")