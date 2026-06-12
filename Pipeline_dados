import pyautogui  #Serve para clicar na tela
import time       #Serve para pausar a execução/esperar algo no processo ser concluido para dar o prox passo
import os         #Serve para o código interagir com o windows
import shutil     #Serve para manipular pastas e arquivos
from datetime import datetime, timedelta  #Serve para manipular data/hora, no meu caso, puxar os dias da semana ATUAL!!!
import pandas as pd

# =========================================================================
# PARTE 1: EXTRAÇÃO (O ROBÔ DO PYAUTOGUI BUSCA OS DADOS NO CPJ)
# =========================================================================

# --- CONFIGURAÇÕES DE ACESSO ---
USUARIO = "SEU_USUARIO"
SENHA = "SUA_SENHA"

# --- 📅 CÁLCULO AUTOMÁTICO SEMPRE DA SEMANA ATUAL (SEGUNDA A SEXTA) ---
hoje = datetime.now()
segunda = hoje - timedelta(days=hoje.weekday())
sexta = segunda + timedelta(days=4)

DATA_INICIAL = segunda.strftime("%d/%m/%Y") 
DATA_FINAL = sexta.strftime("%d/%m/%Y")

# --- CONFIGURAÇÃO DOS CAMINHOS DOS ARQUIVOS ---
ARQUIVO_TEMPORARIO_1 = r"C:\Users\NOME_USUARIO\AppData\Local\Temp\Agenda - Diária com Descrição - Excel.xlsx"
PASTA_DESTINO_AGENDA = r"C:\sua_pasta_rede\Planilhas\Agenda - Diária com Descrição - Excel.xlsx"

ARQUIVO_TEMPORARIO_2 = r"C:\Users\NOME_USUARIO\AppData\Local\Temp\Agenda - Diária com Descrição - Excel.xlsx"
PASTA_DESTINO_CONTROLADORIA = r"C:\sua_pasta_rede\Planilhas\Produtividade semanal da Controladoria.xlsx"

print(f"Período reduzido: {DATA_INICIAL} até {DATA_FINAL}")
print("Abrindo o sistema CPJ...")
Caminho_real = r"C:\DiretorioSistema\sistema.exe"
os.startfile(Caminho_real) 

time.sleep(5) 

print("Forçando foco no campo de Login com clique certeiro...")
pyautogui.click(x=806, y=469) 
time.sleep(1)

print("Digitando dados de acesso...")
pyautogui.write(USUARIO)
time.sleep(0.3)
pyautogui.press("tab") 
time.sleep(0.3)
pyautogui.write(SENHA)
time.sleep(0.3)

print("Clicando em OK...")
pyautogui.click(x=810, y=523)
time.sleep(8) 

print("Fechando la tela de erro do sistema...")
pyautogui.click(x=1042, y=612) 
time.sleep(2)

print("Dando foco na janela de notificações e ativando o CPJ com F6...")
pyautogui.click(x=902, y=523) 
time.sleep(0.5)
pyautogui.press("f6")
time.sleep(3) 

print("Fechando o resumo de tarefas pendentes (Não)...")
pyautogui.hotkey("alt", "n")
time.sleep(2)

print("Fechando a janela de notificações principal...")
pyautogui.click(x=905, y=628) 
time.sleep(3) 

print("Abrindo o Gerador de Relatórios (F5)...")
pyautogui.press("f5")
time.sleep(4) 

print("Selecionando o modelo de Agenda...")
pyautogui.write("agenda", interval=0.1)
time.sleep(1)

for _ in range(6):
    pyautogui.press("down")
    time.sleep(0.4)

pyautogui.press("enter")
time.sleep(4) 

print("Preenchendo os filtros de data...")
pyautogui.press("tab") 
time.sleep(0.5)
pyautogui.write(DATA_INICIAL)
time.sleep(0.5)
pyautogui.press("tab") 
time.sleep(0.5)
pyautogui.write(DATA_FINAL)
time.sleep(0.5)

print("Alterando o filtro 'Solicitado por'...")
pyautogui.press("tab")
time.sleep(0.3)
pyautogui.press("up")
time.sleep(0.5)
pyautogui.press("enter") 

print("Filtros aplicados! Comando final enviado ao CPJ para Relatório 1...")
pyautogui.hotkey("alt", "o")

print("⏳ Aguardando o CPJ gerar o primeiro relatório...")
time.sleep(200) 

print("Fechando instâncias do Excel para liberar o arquivo 1...")
os.system("taskkill /f /im excel.exe >nul 2>&1")
time.sleep(2)

try:
    print("Interceptando o arquivo 1 e movendo para a rede...")
    shutil.move(ARQUIVO_TEMPORARIO_1, PASTA_DESTINO_AGENDA)
    print("✅ Sucesso! Relatório da Agenda Semanal updated.")
    
    print("\n Iniciando a extração do segundo relatório (Controladoria)...")
    time.sleep(2) 
    
    print("Abrindo os filtros do modelo selecionado (Apertando Enter)...")
    pyautogui.press("enter") 
    time.sleep(5) 
    
    print("Preenchendo os filtros de data para a Controladoria...")
    pyautogui.press("tab") 
    time.sleep(0.5)
    pyautogui.write(DATA_INICIAL)
    time.sleep(0.5)
    pyautogui.press("tab") 
    time.sleep(0.5)
    pyautogui.write(DATA_FINAL)
    time.sleep(0.5)
    
    print("Alterando o filtro de 'Pendente' para 'Concluído'...")
    pyautogui.click(x=839, y=380) 
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    
    print("Alterando o filtro para 'Solicitado por'...")
    pyautogui.click(x=1009, y=376) 
    time.sleep(1)
    pyautogui.press("up")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    
    print("Gerando o relatório da Controladoria (Apertando OK)...")
    pyautogui.click(x=1085, y=290)
    
    print("⏳ Aguardando o CPJ gerar o segundo relatório rápido...")
    time.sleep(200) 
    
    print("Fechando instâncias do Excel para liberar o arquivo 2...")
    os.system("taskkill /f /im excel.exe >nul 2>&1")
    time.sleep(2)
    
    print("Interceptando o arquivo 2 e movendo para a rede...")
    shutil.move(ARQUIVO_TEMPORARIO_2, PASTA_DESTINO_CONTROLADORIA)
    print("✅ Sucesso! Relatório da Controladoria atualizado.")
    
    print("\n--- COMBO DE EXTRAÇÃO CONCLUÍDO COM SUCESSO! ---")

    # =========================================================================
    # PARTE 2: TRATAMENTO E CARGA (ETL COM PANDAS)
    # =========================================================================
    print("\n🔄 [ESTÁGIO 2 - TRANSFORM] Iniciando a limpeza dos dados com Pandas...")
    
    # O arquivo que o robô acabou de salvar na rede vira a origem (CAMINHO_BRUTO)
    CAMINHO_BRUTO = PASTA_DESTINO_CONTROLADORIA
    CAMINHO_DESTINO = r"C:\sua_pasta_rede\Planilhas\Produtividade_Final_Tratada.xlsx"
    
    print(f"Lendo o arquivo recém-gerado em: {CAMINHO_BRUTO}")
    df = pd.read_excel(CAMINHO_BRUTO)
    print("✅ Arquivo lido com sucesso!")
    print(f" A base bruta tem {df.shape[0]} linhas e {df.shape[1]} colunas.")

    colunas_originais = ["Status", "ATP.EVE.Descrição", "Responsável", "Interno"]
    df = df[colunas_originais]

    # Ajustado de "ATP#EVE#Descrição" para "ATP.EVE.Descrição" para melhor leitura
    dicionario_nomes = {
        "ATP.EVE.Descrição": "Tarefa"
    }
    df = df.rename(columns=dicionario_nomes)

    df["Status"] = df["Status"].astype(str).str.strip()
    status_desejados = ["Aceito", "Concluído", "Cumprido", "aceito", "concluido", "cumprido"]
    df = df[df["Status"].isin(status_desejados)]

    df["Interno"] = pd.to_datetime(df["Interno"], errors="coerce").dt.date
    print("✅ Filtros de status e data concluídos!")
    print("✅ Colunas desnecessárias removidas!")

    print("\n [ESTÁGIO 3 - LOAD] Salvando o arquivo tratado para o Power BI...")
    df.to_excel(CAMINHO_DESTINO, index=False)

    print(f"\n PIPELINE COMPLETA CONCLUÍDA COM SUCESSO!")
    print(f" Arquivo limpo disponível em: {CAMINHO_DESTINO}")

except Exception as e:
    print(f"\n❌ Erro durante o processo da pipeline: {e}")
