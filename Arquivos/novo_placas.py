#Gerador de placas Mercosul V.2.2
#Conforme Resolução Contran 969/2022 Anexo I

import csv
import os
import datetime
from funcoes_placas import *

# Verifica se as libs necessárias estão instaladas. Instala as libs, se não estiverem.
required_libraries = ['tkinter', 'customtkinter']
instalar_libs(required_libraries)

# Verifica se o arquivo de placas existe. Cria o arquivo, se não existir.
if not os.path.exists("placas.csv"):
    tb1 = open(r"placas.csv", "w")

# Variáveis iniciais necessárias
pl = ""
placas_dia = ()
dia_hoje = datetime.date.today()

# Chama a função menu
opcao = chamar_menu()

# Chama a função escolhida
while opcao in {"E", "N", "T", "A", "D", "P"}:
    if opcao == "N":
        placa = placa_nova()
        print("\nNova placa", placa, "gerada.")
        pl = pl + "," + placa
    elif opcao == "T":
        placa, Pat = troca_placa()
        print("\nPlaca", Pat, "alterada para", placa)
        pl = pl + "," + placa
    elif opcao == "D":
        busca_placas()
    elif opcao == "E":
#        print(pl)
        placas_dia = pl
        grava_placas(dia_hoje, placas_dia)
        print("\nPrograma encerrado.")
        break
    elif opcao == "A":
        ajuda()
        limpar_tela()
        opcao = chamar_menu()
    opcao = chamar_menu()

    limpar_tela() #Chama a função de limpar a tela

