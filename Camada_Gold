-- MP Business Intelligence - Pipeline de Dados Comerciais
-- Modulo: Modelagem de Dados (Camada Gold)
-- Autor: L. Gustavo Gabriel

-- Descricao:
--     Queries responsaveis pela criacao das tabelas de negocio (camada Gold).
--     Estas estruturas alimentam diretamente o modelo Star Schema no Power BI.

-- =========================================================================
-- 1. VISAO DO FUNIL DE VENDAS (Agregado por Status, Tempo e Regiao)
-- =========================================================================
CREATE OR REPLACE TABLE `mp-bi-pipeline.gold.bi_visao_funil` AS
SELECT
    id_lead,
    empresa_cliente,
    status_funil,
    valor_estimado,
    data_cadastro,
    EXTRACT(YEAR FROM data_cadastro) AS ano_cadastro,
    EXTRACT(MONTH FROM data_cadastro) AS mes_cadastro,
    FORMAT_DATE('%B', data_cadastro) AS nome_mes, -- Utilizado para eixos cronologicos
    estado,
    cidade
FROM 
    `mp-bi-pipeline.silver.crm_leads_tratados`;

-- =========================================================================
-- 2. PERFORMANCE DE VENDEDORES (Métricas de Conversao e Ranking)
-- =========================================================================
CREATE OR REPLACE TABLE `mp-bi-pipeline.gold.bi_performance_vendedores` AS
SELECT
    vendedor_interno,
    COUNT(id_lead) AS total_oportunidades,
    
    -- Metricas agregadas para facilitar o calculo de taxa de conversao (Win Rate) no Power BI
    COUNT(CASE WHEN status_funil = 'Ganho' THEN 1 END) AS total_ganhos,
    COUNT(CASE WHEN status_funil = 'Perdido' THEN 1 END) AS total_perdidos,
    
    -- Volume financeiro por vendedor
    SUM(CASE WHEN status_funil = 'Ganho' THEN valor_estimado ELSE 0 END) AS faturamento_total,
    SUM(CASE WHEN status_funil IN ('Prospecção', 'Proposta Enviada', 'Negociação') THEN valor_estimado ELSE 0 END) AS valor_em_pipeline
FROM 
    `mp-bi-pipeline.silver.crm_leads_tratados`
GROUP BY 
    vendedor_interno;
