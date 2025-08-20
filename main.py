import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('gastos.csv')

# Converter a coluna "Data" para datetime
df['Data'] = pd.to_datetime(df['Data'])

# Pedir ao usuário para digitar um mês (no formato: AAAA-MM)
mes_desejado = input("Digite o mês desejado (formato: AAAA-MM, ex: 2025-08): ")

# Filtrar os dados pelo mês informado
df_filtrado = df[df['Data'].dt.strftime('%Y-%m') == mes_desejado]

# Verificar se há dados no mês escolhido
if df_filtrado.empty:
    print("Nenhum gasto encontrado para esse mês.")
else:
    # Total por categoria
    print("Total por categoria:")
    print(df_filtrado.groupby('Categoria')['Valor'].sum())

    # Total por dia
    print("Total por dia:")
    print(df_filtrado.groupby('Data')['Valor'].sum())

    # Gráfico de pizza por categoria
    df_filtrado.groupby('Categoria')['Valor'].sum().plot.pie(autopct='%1.1f%%')
    plt.title(f'Distribuição de Gastos - {mes_desejado}')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()