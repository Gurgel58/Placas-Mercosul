#Gerador de placas Mercosul V.2.0
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
        placa, Pat = troca_placa()
        print("\nPlaca", Pat, "alterada para", placa)
        pl = pl + "," + placa
    elif opcao == "E":
        placas_dia = pl
        grava_placas(dia_hoje, placas_dia)
        print("\nPrograma encerrado.")
        break
    opcao = chamar_menu()
        

