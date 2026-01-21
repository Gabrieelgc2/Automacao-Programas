import os
import subprocess
import time
import pyautogui
import ctypes
import sys

def is_admin():
    """Verifica se o script está rodando como administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
import subprocess

def install_chocolatey():
    print("\n[2/5] Instalando Chocolatey e atualizando PATH...")
    
    # Comando que instala e já tenta atualizar a sessão atual
    command = "Get-ExecutionPolicy"
    checkRestricted = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, shell=False)
    if checkRestricted.returncode == 0:
        print("Command executed successfully:")
        print(checkRestricted.stdout)
        subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy AllSigned"], capture_output=True, text=True, shell=False)
    else:
        print("Command failed to execute:")
        print(checkRestricted.stderr)

    ExecuteChocolatey = subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex"], capture_output=True, text=True, shell=True)
    if ExecuteChocolatey.returncode == 0:
        print("Chocolatey installed successfully.")
        Chocoversion = subprocess.run(["powershell", "-Command", "choco --version"], capture_output=True, text=True, shell=False)
        print("Installed Chocolatey version: ", Chocoversion.stdout)
    else:
        print("Failed to install Chocolatey.")
        print(ExecuteChocolatey.stderr)
        Chocoversion = subprocess.run(["powershell", "-Command", "choco --version"], capture_output=True, text=True, shell=False)

def install_programs():
    # Caminho padrão onde o Chocolatey instala o executável
    choco_path = r"C:\ProgramData\chocolatey\bin\choco.exe"
    
    # Verificamos se o arquivo físico existe antes de tentar rodar
    if os.path.exists(choco_path):
        print("Executando instalação via caminho absoluto...")
        
        cmd = f"& '{choco_path}' install adobereader winrar office365business --yes"
        Programs = subprocess.run(["powershell", "-Command", cmd], shell=False)
        
        if Programs.returncode == 0:
            print("Programs installed successfully.")
        else:
            print("Failed to install some programs.")
    else:
        print("Erro: choco.exe não encontrado no diretório padrão.")

def atualizar_path():
    print("Atualizando variáveis de ambiente...")
    update_cmd = (
        "$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + "
        "[System.Environment]::GetEnvironmentVariable('Path','User')"
    )
    subprocess.run(["powershell", "-Command", update_cmd], shell=True)

def setup_machine():
    if not is_admin():
        print("ERRO: Este script PRECISA ser executado como Administrador.")
        print("Clique com o botão direito no terminal ou no .exe e selecione 'Executar como Administrador'.")
        input("Pressione Enter para sair...")
        sys.exit()

    print("--- Iniciando Automação Profissional (Modo Admin) ---")

    # Instala o Chocolatey e altera privacidades do Powershell
    install_chocolatey()

    print("\n[3/5] Instalando Adobe Reader, WinRAR e Office...")
    install_programs()

    # [4/5] Ativação (MAS)
    print("\n[4/5] Abrindo ativador...")
    os.system("start powershell -NoExit -Command \"irm https://get.activated.win | iex\"")
    
    time.sleep(15)
    
    # [5/5] Tecla automática
    pyautogui.press('1')
    print("Comando '1' enviado.")

    print("\n--- Processo Finalizado! ---")
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    setup_machine()