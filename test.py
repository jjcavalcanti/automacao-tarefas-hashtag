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
    # 1. Clicar no primeiro campo
    pyautogui.click(x=609, y=256)

    # 2. Pegar as informações da linha atual da tabela
    codigo = str(dataframe.loc[linha, "codigo"])
    marca = str(dataframe.loc[linha, "marca"])
    tipo = str(dataframe.loc[linha, "tipo"])
    categoria = str(dataframe.loc[linha, "categoria"])
    preco = str(dataframe.loc[linha, "preco_unitario"])
    custo = str(dataframe.loc[linha, "custo"])
    obs = str(dataframe.loc[linha, "obs"])

    # 3. Preencher os campos usando as variáveis
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")

    pyautogui.write(categoria)
    pyautogui.press("tab")

    pyautogui.write(preco)
    pyautogui.press("tab")

    pyautogui.write(custo)
    pyautogui.press("tab")

    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    # 4. Enviar o formulário
    pyautogui.press("enter")

    # 5. Voltar ao topo da página para a próxima repetição
    pyautogui.scroll(5000)