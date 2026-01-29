import pyautogui
import time
time.sleep(5)
MicrosoftOffice = pyautogui.locateCenterOnScreen('TESTE4.png', confidence=0.8)
pyautogui.click(MicrosoftOffice, button='right')

time.sleep(2)

ExtractZip = pyautogui.locateCenterOnScreen('ExtractZip.png', confidence=0.8)
pyautogui.click(ExtractZip)
time.sleep(3)

Delete = pyautogui.locateCenterOnScreen('Delete.png', confidence=0.8)
pyautogui.press('backspace')
time.sleep(2)

pyautogui.typewrite("C:\\Users\\User\\Downloads\\MicrosoftOfficeAutomacao")
pyautogui.press('enter')

time.sleep(40)

MicrosoftOfficeAutomacao = pyautogui.locateCenterOnScreen('MicrosoftOfficeAutomacao.png', confidence=0.8)
pyautogui.doubleClick(MicrosoftOfficeAutomacao)
time.sleep(1)

MicrosoftOffice5 = pyautogui.locateCenterOnScreen('MicrosoftOffice5.png', confidence=0.8)
pyautogui.doubleClick(MicrosoftOffice5)
time.sleep(1)

setup_icon = pyautogui.locateCenterOnScreen('setup-icon.png', confidence=0.8)
pyautogui.doubleClick(setup_icon)

time.sleep(3)

pyautogui.press('enter')
time.sleep(1)   
continuar = pyautogui.locateCenterOnScreen('continue.png', confidence=0.8)
pyautogui.click(continuar)

time.sleep(2)

installnow = pyautogui.locateCenterOnScreen('installnow.png', confidence=0.8)
pyautogui.click(installnow)
time.sleep(180)
