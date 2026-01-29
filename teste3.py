import os
import time
import pyautogui

time.sleep(5)
print("\n[4/5] Abrindo ativador...")
os.system("start powershell -NoExit -Command \"irm https://get.activated.win | iex\"")

time.sleep(20)
    
# [5/5] Tecla automática
pyautogui.press('2')
print("Comando '2' enviado.")
time.sleep(3)

pyautogui.press('1')
print('Comando "1" enviado para ativar o Office.')
time.sleep(3)       
    
pyautogui.press('enter')
print("Comando 'Enter' enviado para retornar.")
time.sleep(3)

pyautogui.press('0')
print("\n--- Processo Finalizado! ---")