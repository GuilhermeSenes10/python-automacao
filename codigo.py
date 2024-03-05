# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pyautogui -> biblioteca que permite automatizar trabalhos com mouse e teclado
# pip install pyautogui
import pyautogui # pacote de automoção
import time # pacote de tempo

pyautogui.PAUSE = 0.5 #em cada comando

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado
# pyautogui.PAUSE -> pausa entre codigos em segundos

# pyautogui.hotkey("command", "space") duas teclas - abrir no mac

# abrir navegador(chrome, opera GX....)
pyautogui.press("win")
pyautogui.write("opera GX")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3 segundos)
time.sleep(3) #neste ponto

# Passo 2: fazer o login
pyautogui.click(x=923, y=358)
pyautogui.write("teste@gmail.com")

# escrever senha
pyautogui.press("tab")
pyautogui.write("12345")

# confirmar login
pyautogui.press("enter")
time.sleep(3) # margens de segurança para garantir

# Passo 3: importar a base de dados
# pip install pandas numpy openpyxl
import pandas #pacote para representar e trabalhar com dados tabulares
tabela = pandas.read_csv("produtos.csv")

# Passo 4: cadastrar um produto
# para cada linha na minha tabela
for linha in tabela.index:

    # clicar no primeiro campo
    pyautogui.click(x=895, y=239)

    # codigo do produto
    codigo = tabela.loc[linha,"codigo"] #pegando a informação na tabela
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    # categoria
    # str() string - > texto
    # str(1) -> 1 -> "1"

    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    # Preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    # observação
    # pandas.isna -> verifica se está vazia
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000) #rolar a página    
        
 # Passo 5: repetir o processo de cadastro até acabar a base de dados