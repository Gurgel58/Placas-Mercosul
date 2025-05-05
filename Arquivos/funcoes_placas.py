#Gerador de Placas Padrão Mercosul V.2.2
#Conforme Resolução Contran 969/2022 Anexo I
#Funções necessárias
import os


def instalar_libs(required_libraries):
	import sys
	import subprocess
	for lib in required_libraries:
		try:
			__import__(lib)
		except ImportError:
			subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])

# Função para limpar a tela a cada iteração.

def limpar_tela():
	if os.name == "nt":  # Para Windows
		os.system("cls")
	else:  # Para Linux/macOS
		os.system("clear")

def chamar_menu():
	print("\nGerador de Placas Mercosul")
	escolha = input("Digite:\n<N> Para Nova placa\n<T> para Trocar a placa\n<D> busca as placas geradas em uma determinada Data\n<P> busca a data em que uma determinada Placa foi gerada\n<E> para gravar as placas geradas e Encerrar\n<A> para Ajuda: ").upper()
	return escolha

def placa_nova():
	import random
	pl = ""
	for x in range(7):
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
	Pat = input("Informe a placa atual (sem espaços):").upper()
	Pat1 = Pat[0:4]; Pat2 = Pat[5:]; Ptr = Pat[4]; Pat3 = troc.pop(Ptr)
	pl = Pat1 + Pat3 + Pat2
	placa = pl[0:3] + "-" + pl[3:]
	return placa, Pat

def grava_placas(dia_hoje, placas_dia):
	import csv
	dados = list()
	dados_hoje = str(dia_hoje) + placas_dia
	dados.append(dados_hoje)
#	print(dados)
	with open("placas.csv", "a+", newline="") as plc:
		escrever = csv.writer(plc)
		escrever.writerow(dados)
#		plc.writelines(dados)
#		plc.close()
		print("\nPlacas do dia", dia_hoje, "gravadas.")
	return

def busca_placas():
	import csv
	data = input ("\nEntre com a data, no formato AAAA-MM-DD")
	# Busca todas as placas criadas em uma determinada data
	with open("placas.csv", "r", newline="") as plc:
		lista = plc.readlines()
		comp = len(lista)
		resultado = ""
		for linha in lista:
			item_linha = linha.split(",")
			if data == item_linha[0]:
				for x in range(1,len(item_linha)):
					resultado = resultado + item_linha[x] + ","
		if resultado == "":
			print("Nenhuma placa criada na data", data)
		else:
			print("Placas", resultado[:-2], "criadas em", data)
		input("Pressione <Enter> para prosseguir.")
	return

def busca_data():
	import csv
#Busca a data em que uma determinada placa foi criada
	placa_procurada = input("\nEntre com a placa selecionada, no formato AAA-NANN: ").upper()

	with open("placas.csv", "r", newline="") as plc:
		leitor = csv.reader(plc)
		data_encontrada = []

		for linha in leitor:
			for placa in range(len(linha)):
				if linha[placa] == placa_procurada:
					data_encontrada = linha[0]
		if data_encontrada:
			print(f"Placa {placa_procurada} criada em {data_encontrada}")
		else:
			print(f"Placa {placa_procurada} não localizada")
	input("Pressione <Enter> para continuar")
	return

def ajuda():
	print("""
    Gerador de Placas no Padrão Mercosul

    Este programa gera placas de veículos automotores
    no Padrão Mercosul, onde as placas tem o formato AAA-NANN
    (3 letras, um dígito, uma letra, 3 digitos).
    As placas de modelo antigo tem o formato AAANNNN
    (3 letras e 4 digitos).

    Menu de opções:

    <N> para criar uma Nova placa,
    <T> para Trocar uma placa de modelo antigo pelo modelo novo,
    <D> para listar todas as placas criadas em uma determinada Data.
    <P> para informar a data em que uma determinada Placa foi criada.
    <E> grava as placas geradas e Encerrar a criação de placas,
    <A> esta Ajuda.

    Ao escolher a opção <E> uma nova linha será acrescentada ao
    arquivo placas.csv, tendo a data atual como referência.
    Após a gravação o programa é encerrado.

    Todas as datas estão no formato AAAA-MM-DD.

    """)
	input("Tecle <ENTER> para prosseguir.")
	return
