# Gerador de Placas Mercosul    ![Static Badge](https://img.shields.io/badge/Git-Python-green)


### Descrição:

Script Python capaz de gerar novas placas para veículos automotivos, conforme Padrão Mercosul, 
de acordo com a **Resolução Contran 969/2022 Anexo I**, no formato utilizado no Brasil. :brazil:


### Como? 

:arrow_forward: Script dividido em duas partes onde a primeira parte é responsãvel por solicitar a ação a ser
tomada e apresentar os resultados.

:arrow_forward: A segunda parte é responsável pelas ações: **gerar** uma nova placa, **trocar** uma placa modelo
antigo pelo novo modelo e **gravar** as placas geradas durante o dia em um arquivo **CSV**

(A primeira versão **(V.1.0)** não gravava as placas geradas separadas por dia e se utilizava 
apenas de um script, dificultando a leitura)


### ToDo:

:arrow_forward: Completar o código de gravação do arquivo CSV.

:arrow_forward: Criar trecho para verificar se a placa criada já existe.

:arrow_forward: Desenvolver Interface Gráfica (customtkinter).

:arrow_forward: Testes de adequação
