import pandas as pd

# --- Etapa 1: Importação e Preparação ---

# Carregar o arquivo CSV para um DataFrame
# Certifique-se de que o arquivo 'academia_dataset.csv' está na mesma pasta do script
# ou forneça o caminho completo para ele.
try:
    df = pd.read_csv('academia_dataset.csv')
    print("Arquivo 'academia_dataset.csv' carregado com sucesso.\n")
except FileNotFoundError:
    print("Erro: O arquivo 'academia_dataset.csv' não foi encontrado.")
    print("Por favor, verifique se o nome do arquivo está correto e se ele está no diretório certo.")
    exit()

# Criar a coluna 'receita_total' (valor_mensal * tempo_meses)
df['receita_total'] = df['valor_mensal'] * df['tempo_meses']


# --- Etapa 2: Análise Agrupada por Unidade ---

print("--- Análise por Unidade (Academia) ---")
# Agrupar por 'academia' e agregar os dados
analise_unidade = df.groupby('academia').agg(
    quantidade_alunos=('id_aluno', 'count'),
    receita_total=('receita_total', 'sum')
).sort_values('receita_total', ascending=False) # Ordenar pela receita

# Exibir o resultado da análise por unidade
print("Resultado: Quantidade de alunos e Receita Total por Unidade.")
print(analise_unidade)
print("-" * 40 + "\n")


# --- Etapa 3: Análise Agrupada por Plano de Assinatura ---

print("--- Análise por Plano de Assinatura ---")
# Agrupar por 'plano' e agregar os dados
analise_plano = df.groupby('plano').agg(
    numero_de_alunos=('id_aluno', 'count'),
    receita_total=('receita_total', 'sum'),
    tempo_medio_permanencia_meses=('tempo_meses', 'mean')
).sort_values('receita_total', ascending=False) # Ordenar pela receita

# Arredondar o tempo médio para 1 casa decimal
analise_plano['tempo_medio_permanencia_meses'] = analise_plano['tempo_medio_permanencia_meses'].round(1)


# Exibir o resultado da análise por plano
print("Resultado: Alunos, Receita e Permanência Média por Plano.")
print(analise_plano)
print("-" * 40 + "\n")


# --- Etapa 4: Conclusões

print("--- Conclusões da Análise ---")
# Unidade com maior receita
unidade_maior_receita = analise_unidade.index[0]
valor_maior_receita_unidade = analise_unidade['receita_total'].max()
print(f"1. Unidade com Maior Receita: {unidade_maior_receita} (R$ {valor_maior_receita_unidade:,.2f})")

# Plano com maior receita
plano_maior_receita = analise_plano.index[0]
valor_maior_receita_plano = analise_plano['receita_total'].max()
print(f"2. Plano com Maior Receita: {plano_maior_receita} (R$ {valor_maior_receita_plano:,.2f})")

# Perfil dos alunos mais fiéis
plano_maior_fidelidade = analise_plano['tempo_medio_permanencia_meses'].idxmax()
tempo_maior_fidelidade = analise_plano['tempo_medio_permanencia_meses'].max()
print(f"3. Perfil de Aluno Mais Fiel: Assinantes do '{plano_maior_fidelidade}', com permanência média de {tempo_maior_fidelidade} meses.")

# Unidade com desempenho mais fraco
unidade_fraca = analise_unidade.index[-1]
alunos_unidade_fraca = analise_unidade['quantidade_alunos'].min()
print(f"4. Unidade com Potencial de Melhoria: {unidade_fraca}, que possui o menor número de alunos ({alunos_unidade_fraca}).")