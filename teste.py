import pyautogui
import time
time.sleep(4)

microsoftEdge = pyautogui.locateCenterOnScreen('MicrosoftEdge.png', confidence=0.8)
pyautogui.doubleClick(microsoftEdge)
time.sleep(2)

pyautogui.typewrite("https://drive.google.com/drive/folders/1IyNDEgph5LmkgjoEeSFtd6AYNt6X-BSC")
pyautogui.press('enter')
time.sleep(10)

baixarTudo = pyautogui.locateCenterOnScreen('BaixarTudo.png', confidence=0.8)
pyautogui.click(baixarTudo)
time.sleep(180)

AbrirArquivo = pyautogui.locateCenterOnScreen('AbrirArquivo.png', confidence=0.8)
pyautogui.click(AbrirArquivo)
time.sleep(10)

MicrosoftOffice = pyautogui.locateCenterOnScreen('MicrosoftOffice3.png', confidence=0.8)
pyautogui.doubleClick(MicrosoftOffice)
time.sleep(3)

setup_no_icon = pyautogui.locateCenterOnScreen('setup-no-icon.png', confidence=0.8)
pyautogui.doubleClick(setup_no_icon)
time.sleep(3)

extractall = pyautogui.locateCenterOnScreen('extractall.png', confidence=0.8)
pyautogui.click(extractall)
time.sleep(5)

extract = pyautogui.locateCenterOnScreen('extract.png', confidence=0.8)
pyautogui.click(extract)
time.sleep(20)