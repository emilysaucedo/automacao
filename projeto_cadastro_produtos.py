# Passo a Passo do Projeto
# Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
#   Abrir um navegador
pyautogui.PAUSE = 0.8

pyautogui.press("win")
pyautogui.write("CHROME")
pyautogui.press("enter")

#   Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login c email e senha

#   selecionar campo de e-mail
pyautogui.click(x=2563, y=372)
#   escrever o e-mail
pyautogui.write("projetoemily@gmail.com")
pyautogui.press("tab") #passa pro próximo campo
pyautogui.write("suasenha")
pyautogui.press("tab") 
pyautogui.press("enter")
# OU pyautogui.click(x=929, y=549) #clique no botão de login
time.sleep(3)

# Passo 3: Importar a base de produtos para cadastrar

import pandas as pd
tabela = pd.read_csv("produtos.csv") 
#print(tabela)

# Passo 4: Cadastrar um produto

for linha in tabela.index: #linha assume o num da linha da tabela
    pyautogui.click(x=2495, y=255)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.press("tab")
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)

# Passo 5: Repetir o processo até cadastrar todos os produtos
 
    
