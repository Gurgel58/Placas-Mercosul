#Gerador de placas Mercosul
#Conforme Resolução Contran 969/2022 Anexo I
import random
import csv
import os
import datetime
from funcoes_placas import *

if not os.path.exists("placas.csv"):
	tb1 = open(r"placas.csv", "w")
pl = ""
placas_dia = ()
dia_hoje = datetime.date.today()

chamar_menu()
while escolha == "N" or escolha == "T" or escolha == "E":
    if escolha == "N":
        placa_nova
        pl = pl + "," + placa
    elif escolha == "T":
        troca_placa
        pl = pl + "," + placa
    else:
        grava_placas
        print("\nPrograma encerrado.")

