import pandas as pd

print(" Iniciando análise de vendas da cafeteria...\n")

try:

    df = pd.read_csv('02. vendas_cafeteria.csv')
except FileNotFoundError:
    print("Erro: Arquivo '02. vendas_cafeteria.csv' não encontrado.")
    exit()

# Limpeza e conversão de dados
df['data_venda'] = pd.to_datetime(df['data_venda'])
df['receita'] = df['qtd_vendida'] * df['preco_unitario']
df['dia_semana'] = df['data_venda'].dt.day_name()
df['mes'] = df['data_venda'].dt.month_name()


# --- Etapa 2: Análise por Loja ---
print(" Análise de Desempenho por Loja")
analise_loja = df.groupby('loja').agg(
    receita_total=('receita', 'sum'),
    total_itens_vendidos=('qtd_vendida', 'sum')
).sort_values('receita_total', ascending=False)

print("Receita e Itens Vendidos por Loja:")
print(analise_loja)
print("-" * 50 + "\n")


# Etapa 3: Análise por Categoria de Produto ---
print(" Análise de Desempenho por Categoria de Produto")
analise_categoria = df.groupby('categoria_produto').agg(
    receita_total=('receita', 'sum'),
    total_itens_vendidos=('qtd_vendida', 'sum')
).sort_values('receita_total', ascending=False)

print("Receita e Itens Vendidos por Categoria:")
print(analise_categoria)
print("-" * 50 + "\n")


# --- Etapa 4: Análise de Produtos Mais Vendidos ---
print(" Análise dos Produtos Mais Vendidos (Top 5)")
analise_produto = df.groupby('produto').agg(
    receita_total=('receita', 'sum'),
    total_itens_vendidos=('qtd_vendida', 'sum')
).sort_values('receita_total', ascending=False)

print("Top 5 Produtos por Receita Gerada:")
print(analise_produto.head(5))
print("-" * 50 + "\n")


# --- Etapa 5: Análise por Dia da Semana ---
print("Análise de Vendas por Dia da Semana")
analise_dia_semana = df.groupby('dia_semana').agg(
    receita_total=('receita', 'sum')
).sort_values('receita_total', ascending=False)

print("Receita Total por Dia da Semana:")
print(analise_dia_semana)
print("-" * 50 + "\n")


# --- Etapa 6: Conclusões
print("Conclusões e Insights ---")

loja_destaque = analise_loja.index[0]
receita_loja_destaque = analise_loja['receita_total'].max()
print(f"1. Loja Destaque: A loja '{loja_destaque}' foi a que mais gerou receita, com um total de R$ {receita_loja_destaque:,.2f}.")

categoria_destaque = analise_categoria.index[0]
print(f"2. Categoria de Ouro: A categoria '{categoria_destaque}' é a mais rentável da cafeteria.")

produto_campeao = analise_produto.index[0]
print(f"3. Produto Campeão: O '{produto_campeao}' é o item individual que mais traz faturamento.")

dia_pico = analise_dia_semana.index[0]
print(f"4. Dia de Pico: O dia da semana com maior volume de vendas é '{dia_pico}'.")