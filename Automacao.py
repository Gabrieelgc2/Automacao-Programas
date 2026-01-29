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
        print("Comando executado com sucesso:")
        print(checkRestricted.stdout)
        subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy AllSigned"], capture_output=True, text=True, shell=False)
    else:
        print("Comando falhou ao ser executado:")
        print(checkRestricted.stderr)

    ExecuteChocolatey = subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex"], capture_output=True, text=True, shell=True)
    if ExecuteChocolatey.returncode == 0:
        print("Chocolatey instalado com sucesso.")
        Chocoversion = subprocess.run(["powershell", "-Command", "choco --version"], capture_output=True, text=True, shell=False)
        print("Versão do Chocolatey instalada: ", Chocoversion.stdout)
    else:
        print("Falha ao instalar o Chocolatey.")
        print(ExecuteChocolatey.stderr)
        Chocoversion = subprocess.run(["powershell", "-Command", "choco --version"], capture_output=True, text=True, shell=False)

def install_programs():
    # Caminho padrão onde o Chocolatey instala o executável
    choco_path = r"C:\ProgramData\chocolatey\bin\choco.exe"
    
    # Verificamos se o arquivo físico existe antes de tentar rodar
    if os.path.exists(choco_path):
        print("Executando instalação via caminho absoluto...")
        
        cmd = f"& '{choco_path}' install adobereader winrar googlechrome --yes"
        Programs = subprocess.run(["powershell", "-Command", cmd], shell=False)
        
        if Programs.returncode == 0:
            print("Programas instalados com sucesso.")
        else:
            print("Falha ao instalar alguns programas.")
    else:
        print("Erro: choco.exe não encontrado no diretório padrão.")

def atualizar_path():
    print("Atualizando variáveis de ambiente...")
    update_cmd = (
        "$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + "
        "[System.Environment]::GetEnvironmentVariable('Path','User')"
    )
    subprocess.run(["powershell", "-Command", update_cmd], shell=True)

def uninstall_programs():
    print("\nDesinstalando programas desnecessários...")
    
    # Usamos aspas triplas para evitar conflitos com as aspas internas
    # E formatamos a lista para o PowerShell entender como um Array de strings
    apps = [
        "Xbox TCUI", "Xbox Identity Provider", "Xbox", 
        "Microsoft Family", "Solitaire & Casual Games", 
        "Diário Microsoft", "MSN Clima", "Microsoft Clipchamp"
        ]
    

    # Criamos a string do comando formatando a lista para: "App1", "App2"
    apps_str = ", ".join([f'"{app}"' for app in apps])
    
    uninstall_cmd = f"{apps_str} | ForEach-Object {{ winget uninstall --name $_ --silent --accept-source-agreements }}"
    
    try:
        # Usamos check=True para lidar com erros de execução se necessário
        result = subprocess.run(["powershell", "-Command", uninstall_cmd], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Processo de desinstalação finalizado.")
        else:
            print(f"Ocorreram avisos ou erros: {result.stderr}")
            
    except Exception as e:
        print(f"Erro ao executar o subprocesso: {e}")

def setup_machine():
    if not is_admin():
        print("ERRO: Este script PRECISA ser executado como Administrador.")
        print("Clique com o botão direito no terminal ou no .exe e selecione 'Executar como Administrador'.")
        input("Pressione Enter para sair...")
        sys.exit()

    print("--- Iniciando Automação Profissional (Modo Admin) ---")

    # Instala o Chocolatey e altera privacidades do Powershell
    install_chocolatey()

    print("\n[2/5] Instalando Adobe Reader, WinRAR")
    install_programs()

    print("\n[3/5] Removendo aplicativos desnecessários...")
    uninstall_programs()

    # [4/5] Ativação (MAS)
    print("\n[4/5] Abrindo ativador...")
    os.system("start powershell -NoExit -Command \"irm https://get.activated.win | iex\"")
    time.sleep(20)
    
    # [5/5] Tecla automática
    Script = pyautogui.locateCenterOnScreen('Script1.png', confidence=0.8)
    pyautogui.click(Script)
    time.sleep(3)
    pyautogui.press('2')
    print("Comando '2' enviado.")

    time.sleep(3)

    pyautogui.locateCenterOnScreen('OfficeActivation2.png', confidence=0.8)
    pyautogui.press('1')
    print('Comando "1" enviado para ativar o Office.')

    time.sleep(3)       
    
    pyautogui.press('enter')
    print("Comando 'Enter' enviado para retornar.")

    time.sleep(3)

    pyautogui.press('0')
    print("\n--- Processo Finalizado! ---")

if __name__ == "__main__":
    setup_machine()