import subprocess

Chocoversion = subprocess.run(["powershell", "-Command", "choco --version"], capture_output=True, text=True, shell=False)
if Chocoversion.returncode == 0:
    print("Chocolatey is already installed. Version:")
    print(Chocoversion.stdout)
else:
    print("Chocolatey is not installed")