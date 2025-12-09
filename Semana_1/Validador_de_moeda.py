import requests
import urllib3
import time
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LIMITES = {
    'dolar': {'min': 4.80, 'max': 5.50},
    'euro': {'min': 4.80, 'max': 7},
    'bitcoin': {'min': 400000, 'max': 500000},
}

valor_dolar = float(input("Valor/Reais/Dolar: R$ "))
valor_euro = float(input("Valor/Reais/Euro: R$ "))
valor_bitcoin = float(input("Valor/Reais/bitcoin: R$ "))

session = requests.Session()
session.verify = False
session.trust_env = False

arquivo = open("cotacoes.csv", "w")
arquivo.write("Data,Hora,Dolar,Euro,Bitcoin\n")
arquivo.close()

print("\nRobo iniciado. Verificando cotacoes a cada 30 minutos...")

while True:
    try:
        agora = datetime.now()
        data = agora.strftime("%d/%m/%Y")
        hora = agora.strftime("%H:%M:%S")

        print(f"\n[{data} {hora}] Consultando cotacoes...")

        response_dolar = session.get(
            "https://economia.awesomeapi.com.br/json/last/USD-BRL",
            timeout=10
        )
        cotacao_dolar = float(response_dolar.json()["USDBRL"]["bid"])
        dolares = valor_dolar / cotacao_dolar

        response_euro = session.get(
            "https://economia.awesomeapi.com.br/json/last/EUR-BRL",
            timeout=10
        )
        cotacao_euro = float(response_euro.json()['EURBRL']['bid'])
        euro = valor_euro / cotacao_euro

        response_bitcoin = session.get(
            "https://economia.awesomeapi.com.br/json/last/BTC-BRL",
            timeout=10
        )
        cotacao_bitcoin = float(response_bitcoin.json()['BTCBRL']['bid'])
        bitcoin = valor_bitcoin / cotacao_bitcoin

        print(f"Dólar:   R$ {valor_dolar:.2f} = US$ {dolares:.2f} (Cotação: R$ {cotacao_dolar:.2f})")
        print(f"Euro:    R$ {valor_euro:.2f} = EUR$ {euro:.2f} (Cotação: R$ {cotacao_euro:.2f})")
        print(f"Bitcoin: R$ {valor_bitcoin:.2f} = BTC {bitcoin:.8f} (Cotação: R$ {cotacao_bitcoin:.2f})")

        if cotacao_dolar <= LIMITES['dolar']['min']:
            print(f"Dolar Abaixo; Compre R$ {LIMITES['dolar']['min']:.2f} \a")
        elif cotacao_dolar >= LIMITES['dolar']['max']:
            print(f"Dolar Caro; Acima de R$ {LIMITES['dolar']['max']:.2f} \a")

        if cotacao_euro <= LIMITES['euro']['min']:
            print(f"EURO Abaixo; Compre R$ {LIMITES['euro']['min']:.2f} \a")
        elif cotacao_euro >= LIMITES['euro']['max']:
            print(f"EURO Caro; Acima de R$ {LIMITES['euro']['max']:.2f} \a")

        if cotacao_bitcoin <= LIMITES['bitcoin']['min']:
            print(f"Bitcoin Abaixo R$ {LIMITES['bitcoin']['min']:.2f} \a")
        elif cotacao_bitcoin >= LIMITES['bitcoin']['max']:
            print(f"Bitcoin Caro; Acima de R$ {LIMITES['bitcoin']['max']:.2f} \a")

        arquivo = open("cotacoes.csv", "a")
        arquivo.write(f"{data},{hora},{cotacao_dolar:.2f},{cotacao_euro:.2f},{cotacao_bitcoin:.2f}\n")
        arquivo.close()

        print("Salvo em cotacoes.csv")
        print("")
        print("")
        print("")
        print(f"Proxima verificacao em 30 minutos...")
        print("")

        time.sleep(5)
        #time.sleep(1800) 30 minutos

    except KeyboardInterrupt:
        print("\n\nRobozinho interrompido.")
        break

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(300)

