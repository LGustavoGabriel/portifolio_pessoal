# Automacao de Processos e Engenharia de Dados (RPA)

Este repositorio centraliza meus projetos de automacao desenvolvidos em Python, focados em otimizar processos operacionais, auditoria de dados, engajamento de equipe e integracao com ferramentas de Business Intelligence.

---

## Projeto 1: Automacao de Engenharia de Dados Juridicos (CPJ)

Este robo realiza a extracao diaria de relatorios massivos de auditoria (com volumes superiores a 1.600 paginas) de dentro de um sistema ERP juridico corporativo.

### Problemas Resolvidos e Impacto no Negocio
* Eliminacao de Gargalos: Substituicao de um processo manual de extracao de dados que consumia tempo diario da equipe por uma rotina 100% autonoma.
* Pipeline de Dados Preciso: O script realiza o calculo dinamico do periodo da semana atual (segunda a sexta) para aplicar os filtros corretos, garantindo consistencia na extracao de dados historicos.
* Orquestracao e Atualizacao: Configurado para rodar localmente via Agendador de Tarefas do Windows de forma coordenada, disponibilizando os arquivos tratados em rede minutos antes da atualizacao automatica programada nos servidores do Power BI Service.

### Ferramentas Utilizadas
* Python 3 (Linguagem base)
* PyAutoGUI (RPA para manipulacao de interface grafica, cliques em coordenadas especificas e preenchimento de formularios)
* OS e Shutil (Tratamento do sistema operacional para derrubar instancias de programas em segundo plano e movimentar arquivos pesados na rede)

---

## Projeto 2: Robo de Engajamento e Cobranca de Timesheet (Pandion)

Este script foi desenvolvido para automatizar a comunicacao interna e auditoria de horas, realizando disparos individuais de avisos na plataforma de mensageria corporativa (Pandion) para garantir o preenchimento do timesheet.

### Problemas Resolvidos e Impacto no Negocio
* Reducao da Inadimplencia de Lancamentos: Automacao do processo de cobranca de compliance de horas que antes exigia acompanhamento e desgaste manual com a equipe.
* Comunicacao em Escala: O robo varre uma lista dinamica de contatos e executa o fluxo completo (abertura do software, busca pelo usuario, digitacao e envio da mensagem) de forma agil e sem falhas humanas.
* Execucao Agendada: Orquestrado para rodar toda sexta-feira em horarios estrategicos de final de turno atraves do Windows Task Scheduler.

### Ferramentas Utilizadas
* Python 3 (Linguagem base)
* PyAutoGUI (Manipulacao de teclas do sistema operacional, simulacao de digitacao humana e atalhos de teclado)
* Time (Gerenciamento de filas de espera para sincronizar a velocidade do script com a resposta de carregamento do software cliente)
