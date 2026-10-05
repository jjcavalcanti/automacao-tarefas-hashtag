import pyautogui
import time
time.sleep(2)
pyautogui.PAUSE =0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=677, y=370)
pyautogui.press("tab")
pyautogui.write("sua senha muito difil")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

import pandas
dataframe = pandas.read_csv("produtos.csv")
print(dataframe)

for linha in dataframe.index:

    pyautogui.click(x=609, y=256)
    pyautogui.write("MOLO000251")
    pyautogui.press("tab")

    pyautogui.write("Logitech")
    pyautogui.press("tab")

    pyautogui.write("mouse")
    pyautogui.press("tab")

    pyautogui.write("categoria")
    pyautogui.press("tab")

    pyautogui.write("preço")
    pyautogui.press("tab")

    pyautogui.write("custo")
    pyautogui.press("tab")

    pyautogui.write("obs")
    pyautogui.press("tab")

    pyautogui.write("50")
    pyautogui.press("tab")

    pyautogui.press("enviar")
#escrever enviar, pois enter não funciona

