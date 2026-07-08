"""
MP Business Intelligence - Pipeline de Dados Comerciais
Modulo: Ingestao de Dados (Camada Bronze)
Autor: L. Gustavo Gabriel

Descricao:
    Script em Python responsavel pela geracao e simulacao de dados sinteticos de CRM
    com regras de negocio complexas utilizando a biblioteca Faker. Realiza a ingestao 
    automatizada diretamente no Google BigQuery via SDK oficial, utilizando a 
    estrategia de WRITE_TRUNCATE para carga na camada Bronze.
"""

import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker
from google.cloud import bigquery
from google.oauth2 import service_account

print("[MP BI] Iniciando Super Gerador de Dados Comerciais para o BigQuery...")

# 1. Inicializacao do gerador de dados sinteticos (Localidade: Brasil)
fake = Faker('pt_BR')

# 2. Autenticacao e Inicializacao do Cliente BigQuery
# NOTA DE SEGURANCA: O arquivo 'credencial.json' contem chaves privadas do GCP.
# Certifique-se de que este arquivo esteja listado no seu .gitignore para evitar vazamentos.
path_to_json = "credencial.json"
try:
    credentials = service_account.Credentials.from_service_account_file(path_to_json)
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    print("Autenticacao com o GCP realizada com sucesso.")
except Exception as e:
    print(f" Erro na autenticacao. Verifique o arquivo de credenciais: {e}")
    exit()

# 3. Parametrizacao das Regras de Negocio do CRM
vendedores = ["Carlos Silva", "Mariana Costa", "Roberto Almeida", "Fernanda Souza"]
status_opcoes = ["Prospecção", "Proposta Enviada", "Negociação", "Ganho", "Perdido"]

# Distribuicao probabilistica para simular um funil de vendas real do mercado
pesos_status = [30, 25, 20, 15, 10] 

lista_leads = []
total_leads = 500  # Volumetria ideal para stress-test do modelo e relatorios

print(f"📡 Gerando {total_leads} registros comerciais com lógica probabilística...")

# 4. Loop de Construcao do Dataset Sintetico
for i in range(1, total_leads + 1):
    # Aplica os pesos para garantir consistencia estatistica no funil
    status = random.choices(status_opcoes, weights=pesos_status, k=1)[0]
    valor_contrato = round(random.uniform(5000, 75000), 2)
    
    # Janela temporal: Distribuicao de registros ao longo dos primeiros 6 meses de 2026
    data_criacao = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 180))
    
    lead = {
        "id_lead": f"LEAD_{1000 + i}",
        "empresa_cliente": fake.company(),
        "responsavel_venda": fake.name(),
        "vendedor_interno": random.choice(vendedores),
        "valor_estimado": valor_contrato,
        "status_funil": status,
        "data_cadastro": data_criacao.strftime("%Y-%m-%d"),
        "estado": fake.state_abbr(),
        "cidade": fake.city()
    }
    lista_leads.append(lead)

# Estruturacao dos dados em um DataFrame Pandas para manipulacao em memoria
df_crm_completo = pd.DataFrame(lista_leads)

# 5. Pipeline de Carga (Ingestao para a Nuvem)
# Schema de destino na camada de dados brutos (Bronze)
table_id = f"{client.project}.bronze.crm_leads_brutos"

# Configuracao do Job: WRITE_TRUNCATE garante idempotencia limpando a tabela antes da nova carga
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")

print(f"☁️ Injetando dataframe ({len(df_crm_completo)} linhas) na camada Bronze do BigQuery...")

try:
    job = client.load_table_from_dataframe(df_crm_completo, table_id, job_config=job_config)
    job.result()  # Bloqueia a execucao ate que a operacao na nuvem seja concluida
    print(f"SUCESSO! Tabela '{table_id}' atualizada com {len(df_crm_completo)} registros prontos para transformacao!")
except Exception as e:
    print(f"Falha ao injetar dados no BigQuery: {e}")
