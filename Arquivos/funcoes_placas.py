#Gerador de Placas Padrão Mercosul V.2.0
#Conforme Resolução Contran 969/2022 Anexo I
#Funções necessárias

def instalar_libs(required_libraries):
	import sys
	import subprocess
	for lib in required_libraries:
		try:
			__import__(lib)
		except ImportError:
			subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])

def chamar_menu():
	escolha = input("Digite:\n<N> Para Nova placa\n<T> para Trocar a placa\n<E> para Encerrar: ").upper()
	return escolha

def placa_nova():
	import random
	pl = ""
	for x in range(7):
		print(x)
		if x == 3 or x > 4:
			c1 = str(int(random.random() * 10))
		else:
			c1 = chr(int((random.random() * 26) + 65))
		pl = pl + c1
		placa = pl[0:3] + "-" + pl[3:]
	return placa

def troca_placa():
	troc = {"0": "A", "1": "B", "2": "C", "3":"D", "4": "E",
			"5": "F", "6": "G", "7": "H","8": "I", "9": "J"}
	Pat = input("informe a placa atual (sem espaços):").upper()
	Pat1 = Pat[0:4]; Pat2 = Pat[5:]; Ptr = Pat[4]; Pat3 = troc.pop(Ptr)
	pl = Pat1 + Pat3 + Pat2
	placa = pl[0:3] + "-" + pl[3:]
	return placa, Pat

def grava_placas(dia_hoje, placas_dia):
	dados = []
	dados = str(dia_hoje) + placas_dia + "\n"
#	dict = {[str(dia_hoje)]: [placas_dia]}
	print(dados)
	with open("placas.csv", "a") as plc:
		plc.writelines(dados)
	return "\nPlacas do dia", dia_hoje, "gravadas."
