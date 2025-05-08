#Gerador de placas Mercosul V.2.3
#Conforme Resolução Contran 969/2022 Anexo I

import subprocess
import shutil
import os

#Abre concole no Windows
if os.name == "nt":
    subprocess.Popen(['start', 'cmd', '/k', 'python3 novo_placas.py'], shell=True)
else:
#Abre console no Linux:
    possiveis_terminais = ["konsole", "x-terminal-emulator", "xterm", "gnome-terminal", "xfce4-terminal", "lxterminal", "tilix", "alacritty"]

    comando_script = 'bash -c "echo Iniciando...; sleep 2; python3 novo_placas.py; exec bash"'

    for terminal in possiveis_terminais:
        path = shutil.which(terminal)
        if path:
            subprocess.Popen([path, '-e', comando_script])
            break
    else:
        print("Nenhum terminal compatível encontrado.")
