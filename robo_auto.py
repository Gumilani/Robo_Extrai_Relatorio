# Automação de Extração de Relatórios

# Importando as bibliotecas
import pyautogui
import time


pyautogui.PAUSE = 1

#abrindo o Google Chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


#entrando no site desejado

pyautogui.write("https://www.linkedin.com/in/gustavostafocker/") # Link ilustrativo devido a confidencialidade 
pyautogui.press("enter")
time.sleep(26)

pyautogui.PAUSE = 0.1

# Extraindo o primeiro relatorio
i = 0
while i < 54:
    pyautogui.press("tab")
    i = i + 1
pyautogui.hotkey("shift","Fn","F10")

i = 0
while i < 5:
    pyautogui.press("Down")
    i = i + 1
pyautogui.press("Right")

pyautogui.PAUSE = 1

pyautogui.press("enter")
time.sleep (20)
pyautogui.press("enter")
time.sleep (5)

# Abrindo outra aba para que possa extrair mais um relatorio
pyautogui.hotkey("ctrl","t")

#entrando no site desejado

pyautogui.write("https://www.linkedin.com/in/gustavostafocker/") # Link ilustrativo devido a confidencialidade
pyautogui.press("enter")
time.sleep(26)

pyautogui.PAUSE = 0.1

# extraindo o segundo relatorio

i = 0
while i < 54:
    pyautogui.press("tab")
    i = i + 1
pyautogui.hotkey("shift","Fn","F10")

i = 0
while i < 5:
    pyautogui.press("Down")
    i = i + 1
pyautogui.press("Right")

pyautogui.PAUSE = 1

pyautogui.press("enter")
time.sleep (20)
pyautogui.press("enter")
time.sleep (5)

# Abrindo outra aba para que possa extrair mais um relatorio
pyautogui.hotkey("ctrl","t")

#entrando no site desejado

pyautogui.write("https://www.linkedin.com/in/gustavostafocker/") # Link ilustrativo devido a confidencialidade
pyautogui.press("enter")
time.sleep(26)

pyautogui.PAUSE = 0.1


# extraindo o terceiro relatorio

i = 0
while i < 60:
    pyautogui.press("tab")
    i = i + 1
pyautogui.hotkey("shift","Fn","F10")

i = 0
while i < 5:
    pyautogui.press("Down")
    i = i + 1
pyautogui.press("Right")

pyautogui.PAUSE = 1

pyautogui.press("enter")
time.sleep (20)
pyautogui.press("enter")
