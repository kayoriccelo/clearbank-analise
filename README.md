# ClearBank - Análise Financeira com Python

Este projeto é o desafio final do módulo de Análise de Dados e Inteligencia de Negócios da Rocketseat.

## Descrição

Notebook Python que lê um arquivo CSV de transações financeiras, valida e limpa os dados, gera métricas mensais (créditos, débitos, saldo, média, maior e menor valor), identifica transações suspeitas (valor acima de R$ 10.000,00) e exporta um relatório estruturado em JSON.

O dataset gerado contém 24 transações de teste, sendo 6 intencionalmente inválidas para demonstrar a lógica de validação (id vazio, cliente vazio, data inválida, tipo inválido, valor não numérico e valor negativo).

## Como executar

1. Abra o notebook `desafio-final.ipynb` no Google Colab ou Jupyter Notebook.
2. A primeira célula gera automaticamente o arquivo `transacoes.csv` com dados de teste. Não é necessário baixar nem preparar o arquivo manualmente.
3. Execute todas as células em ordem, do início ao fim.
4. Verifique o arquivo `relatorio.json` gerado e o relatório exibido no terminal.

## Requisitos

- Python 3.10 ou superior
- Apenas bibliotecas nativas do Python (csv, json, datetime)

## Saídas

- Relatório formatado no terminal com:
  - Resumo da limpeza (total de linhas lidas, válidas e inválidas)
  - Métricas mensais em ordem cronológica, com valores formatados como moeda brasileira (`R$ 1.234,56`)
  - Lista de transações suspeitas
  - Período analisado (data inicial, final e dias entre extremos)
- Arquivo `relatorio.json` com os dados processados em formato estruturado:
  - `gerado_em` — data da geração do relatório
  - `total_transacoes_validas` — quantidade de transações válidas
  - `total_transacoes_invalidas` — quantidade de transações inválidas
  - `resumo_mensal` — métricas agrupadas por mês
  - `transacoes_suspeitas` — transações com valor acima do limite
  - `periodo_analisado` — data inicial, final e dias entre extremos
- (Opcional) `grafico.png` com visualização dos dados

## Opcionais

A pasta `scripts/` contém:
- `analise_pandas.py` — versão alternativa usando pandas, com comparação automática contra a solução nativa
- `grafico.py` — script que gera o `grafico.png` com matplotlib

## Estrutura do notebook

1. Markdown com título e instruções
2. Geração do dataset `transacoes.csv`
3. Importação de bibliotecas nativas
4. Constantes e configurações globais
5. Função `ler_transacoes()` — leitura do CSV com tratamento de `FileNotFoundError`
6. Funções `validar_data()`, `validar_valor()` e `validar_transacao()` — validação completa do registro
7. Função `gerar_relatorio()` — agrupamento mensal, métricas e identificação de suspeitas
8. Função `salvar_json()` — exportação para JSON com metadados de geração
9. Funções `formatar_moeda()` e `exibir_relatorio()` — formatação brasileira e exibição no terminal
10. Execução principal — orquestração completa do pipeline
11. Validação do `relatorio.json` gerado
