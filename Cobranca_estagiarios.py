import pyautogui 
import time

# ==========================================
# CONFIGURAÇÕES INICIAIS
# ==========================================
# Lista de contatos mapeados para envio no Pandion
LISTA_CONTATOS = [
    "colaborador.A@empresa.com.br", 
    "colaborador.B@empresa.com.br",
    "colaborador.C@empresa.com.br"
]

MENSAGEM = "Fala pessoal! Passando para lembrar que hoje é sexta-feira, dia de lançar o timesheet no CPJ! Não vamos esquecer, hein? Valeu!"

# Tempo para clicar na tela antes do robô começar
print("O robô vai começar em 5 segundos. Abra a tela do seu Windows!")
time.sleep(5)

# ==========================================
# AQUI COMEÇA O TRABALHO DO ROBÔ
# ==========================================

for contato in LISTA_CONTATOS:
    print(f"💬 Enviando cobrança para: {contato}")
    
    # 1. Abre a busca do Windows para achar o Pandion
    pyautogui.press('win')
    time.sleep(1) 
    
    pyautogui.write('Pandion')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2) # Espera o Pandion abrir e o cursor piscar na busca
    
    # 2. Digita o contato direto (já que o Pandion abre focado na busca!)
    pyautogui.write(contato)
    time.sleep(1)
    pyautogui.press('enter') # Dá Enter para abrir a janela de chat da pessoa
    time.sleep(1.5) 
    
    # 3. Escreve a mensagem no chat e envia
    pyautogui.write(MENSAGEM)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1) 
    
    print(f"✅ Mensagem enviada para {contato}!")

print("\n TODAS AS COBRANÇAS FORAM ENVIADAS COM SUCESSO!")
