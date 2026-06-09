import pyautogui
import time
import os
import shutil
from datetime import datetime, timedelta

# --- CONFIGURAÇÕES DE ACESSO ---
USUARIO = "SEU_USUARIO_AQUI"
SENHA = "SUA_SENHA_AQUI"

# --- 📅 CÁLCULO AUTOMÁTICO DA SEMANA ATUAL (SEGUNDA A SEXTA) ---
hoje = datetime.now()
# Descobre quantos dias faltam para voltar para a segunda-feira desta semana (hoje.weekday() dá 0 para segunda, 1 para terça...)
segunda = hoje - timedelta(days=hoje.weekday())
sexta = segunda + timedelta(days=4)

DATA_INICIAL = segunda.strftime("%d/%m/%Y") 
DATA_FINAL = sexta.strftime("%d/%m/%Y")

# --- CONFIGURAÇÃO DOS CAMINHOS DOS ARQUIVOS ---
# Primeiro Relatório (Agenda Semanal)
ARQUIVO_TEMPORARIO_1 = r"C:\Users\USUARIO_SISTEMA\AppData\Local\Temp\Agenda - Diária com Descrição - Excel.xlsx"
PASTA_DESTINO_AGENDA = r"C:\Destino_Planilhas\Agenda - Diária com Descrição - Excel.xlsx"
# Segundo Relatório (Controladoria)
ARQUIVO_TEMPORARIO_2 = r"C:\Users\USUARIO_SISTEMA\AppData\Local\Temp\Agenda - Diária com Descrição - Excel.xlsx"
PASTA_DESTINO_CONTROLADORIA = r"C:\Destino_Planilhas\Produtividade semanal da Controladoria.xlsx"


print(f"Período reduzido: {DATA_INICIAL} até {DATA_FINAL}")

# =========================================================================
# PASSO 1: ABRIR O CPJ E FAZER LOGIN
# =========================================================================
print("Abrindo o sistema CPJ...")
Caminho_real = r"C:\CPJ3C_Client\cpj3cclient.exe"
os.startfile(Caminho_real) 

time.sleep(5) # Tempo para a janela carregar totalmente no fundo

print("Forçando foco no campo de Login com clique certeiro...")
# 📍 MINHA COORDENADA: Dá um clique no campo de Usuário para o foco não ir pro VS Code
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

# =========================================================================
# PASSO 2: TRATANDO AS JANELAS INICIAIS
# =========================================================================
print("Fechando a tela de erro do sistema...")
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

# =========================================================================
# PASSO 3: GERADOR DE RELATÓRIOS (RLATÓRIO AGENDA SEMANAL - PENDENTES)
# =========================================================================
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

print("⏳ Aguardando o CPJ gerar o primeiro relatório rápido...")
time.sleep(160) 

print("Fechando instâncias do Excel para liberar o arquivo 1...")
os.system("taskkill /f /im excel.exe >nul 2>&1")
time.sleep(2)

try:
    print("Interceptando o arquivo 1 e movendo para a rede...")
    shutil.move(ARQUIVO_TEMPORARIO_1, PASTA_DESTINO_AGENDA)
    print("✅ Sucesso! Relatório da Agenda Semanal updated.")
    
    # =========================================================================
    # PASSO 4: SEGUNDO RELATÓRIO (CONTROLADORIA - CONCLUÍDOS)
    # =========================================================================
    print("\n🤖 Iniciando a extração do segundo relatório (Controladoria)...")
    time.sleep(2) 
    
    print("Abrindo os filtros do modelo selecionado (Apertando Enter)...")
    pyautogui.press("enter") 
    time.sleep(5) 
    
    # --- 1. PREENCHENDO AS DATAS NO SEGUNDO RELATÓRIO ---
    print("Preenchendo os filtros de data para a Controladoria...")
    pyautogui.press("tab") 
    time.sleep(0.5)
    pyautogui.write(DATA_INICIAL)
    time.sleep(0.5)
    pyautogui.press("tab") 
    time.sleep(0.5)
    pyautogui.write(DATA_FINAL)
    time.sleep(0.5)
    
    # --- 2. ALTERANDO O STATUS PARA "CONCLUÍDO" ---
    print("Alterando o filtro de 'Pendente' para 'Concluído'...")
    pyautogui.click(x=839, y=380) 
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    
    # --- 3. ALTERANDO PARA "SOLICITADO POR" ---
    print("Alterando o filtro para 'Solicitado por'...")
    # 📍 MINHA COORDENADA: Dá o clique exato para abrir a lista sem perder o foco
    pyautogui.click(x=1009, y=376) 
    time.sleep(1)
    
    # Garante a seleção correta da opção dentro do menu aberto
    pyautogui.press("up")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    
    # --- 4. AQUI VAI GERAR O SEGUNDO RELATÓRIO ---
    print("Gerando o relatório da Controladoria (Apertando OK)...")
    # 📍 NOVA COORDENADA: Clique no botão OK do canto superior direito
    pyautogui.click(x=1085, y=290)
    
    print("⏳ Aguardando o CPJ gerar o segundo relatório rápido...")
    time.sleep(140) 
    
    print("Fechando instâncias do Excel para liberar o arquivo 2...")
    os.system("taskkill /f /im excel.exe >nul 2>&1")
    time.sleep(2)
    
    print("Interceptando o arquivo 2 e movendo para a rede...")
    shutil.move(ARQUIVO_TEMPORARIO_2, PASTA_DESTINO_CONTROLADORIA)
    print("✅ Sucesso! Relatório da Controladoria atualizado.")
    
    print("\n--- 🏆 COMBO DE EXTRAÇÃO CONCLUÍDO COM SUCESSO! ---")

except Exception as e:
    print(f"\n❌ Erro durante o processo oculto: {e}")
