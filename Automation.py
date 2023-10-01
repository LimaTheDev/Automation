import pyautogui
import time
import pandas as pd
#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui,hotkey


pyautogui.PAUSE = 0.3

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
time.sleep(2)


tabela = pd.read_csv("F:\intensivos\HashtagPython\Aula 1\Automation\produtos.csv")

print(tabela)

for linha in tabela.index:

    pyautogui.click(x=739, y=286)
    
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
        
    
     
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(marca))
    pyautogui.press("tab")

    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    pyautogui.write(str(preco))
    pyautogui.press("tab")

    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000)
    
enviar_email()