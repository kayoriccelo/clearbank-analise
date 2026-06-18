import pandas as pd
import matplotlib.pyplot as plt

ARQUIVO_CSV = 'transacoes.csv'
ARQUIVO_GRAFICO = 'grafico.png'


def anotar_barras(ax, barras):
    for barra in barras:
        altura = barra.get_height()

        ax.annotate(
            f'R$ {altura:,.0f}'.replace(',', '.'),
            xy=(barra.get_x() + barra.get_width() / 2, altura),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center', va='bottom', fontsize=8
        )


df = pd.read_csv(ARQUIVO_CSV)

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
df_validas['mes'] = df_validas['data'].dt.strftime('%Y-%m')

resumo = df_validas.groupby(['mes', 'tipo'])['valor'].sum().unstack(fill_value=0)
resumo['saldo'] = resumo['credito'] - resumo['debito']

fig, ax = plt.subplots(figsize=(10, 6))

meses = resumo.index
largura = 0.35
x = range(len(meses))

barras_credito = ax.bar([i - largura/2 for i in x], resumo['credito'], largura, label='Crédito', color='#2ecc71')
barras_debito = ax.bar([i + largura/2 for i in x], resumo['debito'], largura, label='Débito', color='#e74c3c')

ax.set_xlabel('Mês')
ax.set_ylabel('Valor (R$)')
ax.set_title('Crédito vs Débito por Mês - ClearBank')
ax.set_xticks(x)
ax.set_xticklabels(meses)
ax.legend()
ax.grid(axis='y', alpha=0.3)

anotar_barras(ax, barras_credito)
anotar_barras(ax, barras_debito)

plt.tight_layout()
plt.savefig(ARQUIVO_GRAFICO, dpi=150, bbox_inches='tight')
print(f"Gráfico salvo em: {ARQUIVO_GRAFICO}")
