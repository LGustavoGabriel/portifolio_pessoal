-- MP Business Intelligence - Pipeline de Dados Comerciais
-- Modulo: Transformacao de Dados (Camada Silver)
-- Autor: L. Gustavo Gabriel

-- Descricao:
--     Query responsavel pela limpeza, padronizacao e garantia de integridade
--     dos dados brutos vindos do CRM (Camada Bronze). Cria a tabela consolidada crm_leads_tratados.

CREATE OR REPLACE TABLE `mp-bi-pipeline.silver.crm_leads_tratados` AS
SELECT
    DISTINCT
    id_lead,
    UPPER(empresa_cliente) AS empresa_cliente, -- Padroniza o nome da empresa em maiusculo
    responsavel_venda,
    vendedor_interno,
    valor_estimado,
    status_funil,
    PARSE_DATE('%Y-%m-%d', data_cadastro) AS data_cadastro, -- Garante o tipo DATE para eixos temporais
    estado,
    cidade
FROM 
    `mp-bi-pipeline.bronze.crm_leads_brutos`
WHERE 
    id_lead IS NOT NULL; -- Garante a integridade da chave primaria
