#Gerador de placas Mercosul V.1.0
#Conforme Resolução Contran 969/2022 Anexo I
import random
import csv
import os
if not os.path.exists("placas.csv"):
	tb1 = open(r"placas.csv", "w")
pl = ""
troc = {"0": "A", "1": "B", "2": "C", "3":"D", "4": "E",
        "5": "F", "6": "G", "7": "H","8": "I", "9": "J"}
flg = False
Tpl = input("Placa [N]ova ou [T]roca? ")
while Tpl.lower() != "n" and Tpl.lower() != "t":
    print("\nInválido. Digite N ou T")
    Tpl = input("\nPlaca [N]ova ou [T]roca? ")
if Tpl.lower() == "n":
    for x in range(7):
        print(x)
        if x == 3 or x > 4:
            c1 = str(int(random.random() * 10))
        else:
            c1 = chr(int((random.random() * 26) + 65))
        
        pl = pl + c1
else:
    Pa = input("informe a placa atual (sem espaços):")
    Pat = Pa.upper()
    Pat1 = Pat[0:4]; Pat2 = Pat[5:]; Ptr = Pat[4]; Pat3 = troc.pop(Ptr)
    pl = Pat1 + Pat3 + Pat2
placa = pl[0:3] + " " + pl[3:]
#pfim = pfim + placa
with open("placas.csv", "r") as plc:
    Lplc = csv.reader(plc)
    for linha in Lplc:
        if linha[0] == placa:
            flg = True
        else:
            pass
with open("placas.csv", "a", newline="") as plc:
    if not(flg):
        Eplc = csv.writer(plc)
        Eplc.writerow([placa])
        print("Placa", placa, "gerada.")
    else:
        print("Placa já existente.")

