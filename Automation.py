import pyautogui
import time

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
time.sleep(3)

pyautogui.click(x=850, y=400)
email = ("Junior371098@gmail.com")
pyautogui.write(email)

pyautogui.click(x=809, y=494)
senha = ("12345678")
pyautogui.write(senha)

pyautogui.click(x=984, y=551)
pyautogui.press("enter")
time.sleep(3)