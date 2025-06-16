import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# vamo carregar os bagulho certinho e preparar os dados
df = pd.read_csv('03. streaming_usuarios.csv')
df.rename(columns={'horas_assistidos': 'tempo_medio_diario'}, inplace=True)

# medir as estatisticas

media_geral = df['idade','tempo_medio_diario'].mean()
desvio_padrao_geral = df[['idade', 'tempo_medio_diario']].std()

jovens = df[df['idade'] < 30]
adultos = df[df['idade'] >= 30]

status_jovens = jovens['tempo_medio_diario'].agg(['mean', 'std'])
status_adultos = adultos['tempo_medio_diario'].agg(['mean', 'std'])

# relacionando
correlacao = df[['idade', 'tempo_medio_diario']].corr()
corr_valor = correlacao.loc['idade', 'tempo_medio_diario']

#grafico gerado
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='idade', y='tempo_medio_diario',
            scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Correlação entre Idade e Tempo Médio de Uso Diário')
plt.xlabel('Idade')
plt.ylabel('Tempo Médio Diário (horas)')
plt.grid(True)
plt.savefig('correlacao_idade_uso.png')

#exibindo so resultados
print("--- Apresentando os resultados ---")
print("\n Medias e desvios por variavel: ")
print(f"Idade - media {media_geral['idade']:.1f} anos, desvio padrao {desvio_padrao_geral['idade']:.1f} anos")
print(f"Tempo de Uso: Média {media_geral['tempo_medio_diario']:.1f} horas, Desvio Padrão {desvio_padrao_geral['tempo_medio_diario']:.1f} horas")

print("\n Correlações : ")
print(f"A correlação entre idade e tempo medio de uso eh {corr_valor:.4f}")
print("\n Este valor é proximo a zero,indicando uma corelação fraca entre as variaveis.")

print("\n Diferença entre jovens e adultos: ")
print(f"Jovens: media {status_jovens['mean']:.1f} horas, desvio padrao {status_jovens['std']:.1f}")
print(f"Adultos: media {status_adultos['mean']:.1f} horas, desvio padrao {status_adultos['std']:.1f}")
print("Não há grande diferença entre a media de uso ou na dispersão dos dados entre faixas etarias..")

