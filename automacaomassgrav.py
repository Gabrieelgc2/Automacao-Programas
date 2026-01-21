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

install_chocolatey()