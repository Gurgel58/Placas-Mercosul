#Gerador de placas Mercosul
#Conforme Resolução Contran 969/2022 Anexo I

import csv
import os
import datetime
from funcoes_placas import *

if not os.path.exists("placas.csv"):
    tb1 = open(r"placas.csv", "w")
pl = ""
placas_dia = ()
dia_hoje = datetime.date.today()

opcao = chamar_menu()
while opcao == "E" or opcao == "N" or opcao == "T":
    if opcao == "N":
        placa = placa_nova()
        print("\nNova placa", placa, "gerada.")
        pl = pl + "," + placa
    elif opcao == "T":
        placa = troca_placa()
        pl = pl + "," + placa
    elif opcao == "E":
        grava_placas
        print("\nPrograma encerrado.")
        break
    else:
        opcao = chamar_menu()
        

