import subprocess

ExecuteChocolatey = subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex"], capture_output=True, text=True, shell=True)
if ExecuteChocolatey.returncode == 0:
    print("Chocolatey installed successfully.")
    Chocoversion = subprocess.run(["powershell", "-Command", "choco --version"], capture_output=True, text=True, shell=False)
    print("Installed Chocolatey version: ", Chocoversion.stdout)
else:
    print("Failed to install Chocolatey.")
    print(ExecuteChocolatey.stderr)