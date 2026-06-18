# ClearBank - Análise Financeira com Python

Este projeto é o desafio final do módulo de Análise de Dados e Inteligencia de Negócios da Rocketseat.

## Descrição

Notebook Python que lê um arquivo CSV de transações financeiras, valida e limpa os dados, gera métricas mensais (créditos, débitos, saldo, média, maior e menor valor), identifica transações suspeitas (valor acima de R$ 10.000,00) e exporta um relatório estruturado em JSON.

## Como executar

1. Abra o notebook `desafio-final.ipynb` no Google Colab ou Jupyter Notebook.
2. Certifique-se de que o arquivo `transacoes.csv` está na mesma pasta (a primeira célula do notebook gera o arquivo automaticamente).
3. Execute todas as células em ordem, do início ao fim.
4. Verifique o arquivo `relatorio.json` gerado e o relatório exibido no terminal.

## Requisitos

- Python 3.10 ou superior
- Apenas bibliotecas nativas do Python (csv, json, datetime)

## Saídas

- Relatório formatado no terminal com:
  - Resumo da limpeza (total de linhas lidas, válidas e inválidas)
  - Métricas mensais (transações, crédito, débito, saldo, média, maior e menor valor)
  - Lista de transações suspeitas
  - Período analisado (data inicial, final e dias entre extremos)
- Arquivo `relatorio.json` com os dados processados em formato estruturado
- (Opcional) `grafico.png` com visualização dos dados

## Opcionais

A pasta `scripts/` contém:
- `analise_pandas.py` — versão alternativa usando pandas, com comparação automática contra a solução nativa
- `grafico.py` — script que gera o `grafico.png` com matplotlib

## Estrutura do notebook

1. Geração do dataset `transacoes.csv`
2. Importação de bibliotecas nativas
3. Constantes e configurações globais
4. Função `ler_transacoes()` - leitura do CSV
5. Função `validar_transacao()` - validação e limpeza
6. Função `gerar_relatorio()` - agrupamento mensal e métricas
7. Função `salvar_json()` - exportação para JSON
8. Função `exibir_relatorio()` - formatação do terminal
9. Execução principal - orquestração completa
10. Validação do `relatorio.json` gerado
