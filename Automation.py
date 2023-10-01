import pyautogui
import time
import pandas as pd
#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui,hotkey


pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=850, y=400)
email = ("Junior371098@gmail.com")
pyautogui.write(email)

pyautogui.click(x=809, y=494)
senha = ("12345678")
pyautogui.write(senha)

pyautogui.click(x=984, y=551)
pyautogui.press("enter")
time.sleep(3)


tabela = pd.read_csv("F:\intensivos\HashtagPython\Aula 1\Automation\produtos.csv")

print(tabela)

time.sleep(2)

pyautogui.click(x=739, y=286)

pyautogui.write("Codigo")
pyautogui.press("tab")

pyautogui.write("Marca")
pyautogui.press("tab")

pyautogui.write("Tipo")
pyautogui.press("tab")

pyautogui.write("Categoria")
pyautogui.press("tab")

pyautogui.write("Preco")
pyautogui.press("tab")

pyautogui.write("Custo")
pyautogui.press("tab")

pyautogui.write("Obs")
pyautogui.press("tab")

pyautogui.press("enter")

pyautogui.scroll(500)