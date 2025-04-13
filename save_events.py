import os
from datetime import datetime

hora_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Função para inserir os registros reconhecidos pela IA no arquivo
def guarda_registros(registro):
    arquivo = "registros.txt"
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as inserir:
            pass

    with open(arquivo, "a") as inserir:
        inserir.write(f"[{hora_registro}] {registro}")
    inserir.close()

# Função para contar a quantidade de ocorrencias de cada evento
def contar_registros():
    arquivo = "registros.txt"
    dic_eventos = {
        "Normaly": 0,
        "Usando Celular": 0,
        "Com sono": 0,
        "Looking Around": 0, 
        "Not Found": 0
    }
   
    for x in dic_eventos:
        with open(arquivo, "r") as contagem:
            event = contagem.read()
            contado = event.count(x)
        dic_eventos[x] = contado

    print("Quantidade de registros:")
    print("Com sono: ",dic_eventos["Com sono"])
    print("Looking around: ",dic_eventos["Looking Around"])
    print("Normally: ", dic_eventos["Normaly"])
    print("Usando Celular: ",dic_eventos["Usando Celular"])
    print("Not Found: ", dic_eventos["Not Found"])