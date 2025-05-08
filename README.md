# Gerador de Placas Mercosul    ![Static Badge](https://img.shields.io/badge/Git-Python-green)


### Descrição:

Script Python capaz de gerar novas placas para veículos automotivos, conforme Padrão Mercosul, 
de acordo com a **Resolução Contran 969/2022 Anexo I**, no formato utilizado no Brasil. :brazil:

O script era previsto para ter uma interface gráfica, gerada em **Customtkinter** porém verificou-se
que o mesmo funcionava melhor apenas usando a console, sendo então mantido seu funcionamento em modo **CLI**.


### Como? 

:arrow_forward: Script dividido em três partes onde a primeira parte é responsável por verificar se o script está sendo executado em 
um ambiente **Linux** ou **Windows**. Caso o ambiente seja o **Linux**, o script verifica qual console de texto está instalada, dentre várias opções
e abre a console disponível, para execuão do restante do aplicativo. Caso o ambiente seja o **Windows**, a console de comando é executada.

▶️ A segunda parte é responsãvel por solicitar a ação a ser tomada e apresentar os resultados. 
Essa parte também é responsável por verificar a existência do arquivo **placas.csv**, onde ficam armazenadas as placas geradas, a cada dia.
Caso o arquivo não existe, o script cria o arquivo, na mesma pasta onde o script está.

:arrow_forward: A terceira parte é responsável pelas ações: **gerar** uma nova placa, **trocar** uma placa modelo
 antigo pelo novo modelo, efetuar buscas no arquivo **placas,csv**, buscando por **data** ou por **placa**,
 **gravar** as placas geradas durante o dia, no arquivo **placas.csv**

 ▶️ É importante notar que, até o presente momento, todos os scripts que compõe o aplicativo devem estar na mesma pasta e o arquivo
 **placas.csv** será gerado e mantido nessa mesma pasta.

 ▶️ ▶️ **IMPORTANTE:** O aplicativo deve ser executado a partir do script **placas.sh**, caso em ambiente **Linux** ou pelo script 
 **placas.bat**, caso em ambiente **Windows**.

### Versões:

**V.1.0** - não gravava as placas geradas separadas por dia e se utilizava apenas de um script, dificultando a leitura.

**V.2.0** - Gerava novas placas ou trocada o modelo antigo pelo novo. Também gravava as placas geradas, separadas por data.

**V.2.1** - Incorporada a **Ajuda** (opção A, no menu).

**V.2.2** - Acréscimo das funções de busca por **Data** e busca por **Placa**.

**V.2.3** - Criação do trecho de código que identifica o ambiente (**Linux** ou **Windows**) e abre a console de texto correspondente.
            Também foram criados os scripts de execução inicial, **placas.sh** e **placas.bat**, de acordo com o ambiente de execução
            **Linux** ou **Windows**, respectivamente.

### ToDo:

:arrow_forward: ~~Completar o código de gravação do arquivo CSV.~~ - :white_check_mark:

:arrow_forward: ~~Desenvolver Interface Gráfica (customtkinter).~~ - Execução será mantida em modo **CLI**

:arrow_forward: Criar trecho para verificar se a placa criada já existe.

▶️ ~~Criar trecho para fazer busca por placa ou por placas criadas em uma determinada data.~~ - :white_check_mark:

▶️ ~~Criar trecho para verificar o ambiente (**Linux** ou **Windows**) e abre a console correspondente.~~ - :white_check_mark:

:arrow_forward: Testes de adequação no **Linux** e no **Windows**.
