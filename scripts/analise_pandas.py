import pandas as pd
import json

ARQUIVO_CSV = 'transacoes.csv'
ARQUIVO_JSON = 'relatorio.json'
LIMITE_SUSPEITO = 10000.00


df = pd.read_csv(ARQUIVO_CSV)

print("Total de linhas lidas:", len(df))

df['id'] = pd.to_numeric(df['id'], errors='coerce')
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
df['data'] = pd.to_datetime(df['data'], errors='coerce', format='%Y-%m-%d')

filtro = (
    df['id'].notna() &
    df['cliente_id'].notna() & (df['cliente_id'].astype(str).str.strip() != '') &
    df['data'].notna() &
    df['tipo'].isin(['credito', 'debito']) &
    df['valor'].notna() & (df['valor'] > 0)
)

df_validas = df[filtro].copy()
total_invalidas = len(df) - len(df_validas)

print("Linhas válidas:", len(df_validas))
print("Linhas inválidas:", total_invalidas)

df_validas['mes'] = df_validas['data'].dt.strftime('%Y-%m')

resumo = df_validas.groupby('mes').agg(
    quantidade=('id', 'count'),
    total_credito=('valor', lambda x: x[df_validas.loc[x.index, 'tipo'] == 'credito'].sum()),
    total_debito=('valor', lambda x: x[df_validas.loc[x.index, 'tipo'] == 'debito'].sum())
).reset_index()

resumo['saldo'] = resumo['total_credito'] - resumo['total_debito']
resumo['media'] = df_validas.groupby('mes')['valor'].mean().values
resumo['maior_valor'] = df_validas.groupby('mes')['valor'].max().values
resumo['menor_valor'] = df_validas.groupby('mes')['valor'].min().values

resumo = resumo.round({'total_credito': 2, 'total_debito': 2, 'saldo': 2, 'media': 2, 'maior_valor': 2, 'menor_valor': 2})

print("\n===== RESUMO MENSAL (PANDAS) =====")
print(resumo.to_string(index=False))

suspeitas = df_validas[df_validas['valor'] > LIMITE_SUSPEITO][['id', 'cliente_id', 'data', 'valor']].copy()
suspeitas['data'] = suspeitas['data'].dt.strftime('%Y-%m-%d')

print("\n===== TRANSAÇÕES SUSPEITAS (PANDAS) =====")
if not suspeitas.empty:
    print(suspeitas.to_string(index=False))
else:
    print("Nenhuma transação suspeita encontrada.")

data_inicial = df_validas['data'].min().strftime('%Y-%m-%d')
data_final = df_validas['data'].max().strftime('%Y-%m-%d')
dias_entre_extremos = (df_validas['data'].max() - df_validas['data'].min()).days

print(f"\nPeríodo: {data_inicial} a {data_final} ({dias_entre_extremos} dias)")

with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
    relatorio_nativo = json.load(f)

print("\n===== COMPARAÇÃO NATIVO vs PANDAS =====")
for mes in sorted(relatorio_nativo['resumo_mensal'].keys()):
    nativo = relatorio_nativo['resumo_mensal'][mes]
    pandas_row = resumo[resumo['mes'] == mes].iloc[0]

    assert nativo['quantidade'] == pandas_row['quantidade'], f"quantidade diverge em {mes}"
    assert nativo['total_credito'] == pandas_row['total_credito'], f"total_credito diverge em {mes}"
    assert nativo['total_debito'] == pandas_row['total_debito'], f"total_debito diverge em {mes}"
    assert nativo['saldo'] == pandas_row['saldo'], f"saldo diverge em {mes}"
    assert nativo['maior_valor'] == pandas_row['maior_valor'], f"maior_valor diverge em {mes}"
    assert nativo['menor_valor'] == pandas_row['menor_valor'], f"menor_valor diverge em {mes}"

    print(f"{mes}: OK")

print("\nTodos os valores batem entre nativo e pandas!")
