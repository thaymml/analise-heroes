import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('data/heroes.csv', encoding='ISO-8859-1', delimiter=';')

print(df.columns)

df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
df['Strength'] = pd.to_numeric(df['Strength'], errors='coerce')

df['Strength'].fillna(0, inplace=True)

df['First appearance'] = df['First appearance'].astype(str)

df['Year'] = df['First appearance'].str.extract(r'(\d{4})').astype(float)

# 1. Gráfico de Barras: Distribuição por Editora
plt.figure(figsize=(10, 6))
df['Publisher'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribuição de Personagens por Editora', fontsize=16)
plt.xlabel('Editora', fontsize=12)
plt.ylabel('Número de Personagens', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# 2. Gráfico de Dispersão: Altura x Peso
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Height', y='Weight', hue='Strength', palette='viridis', size='Strength', sizes=(20, 200))
plt.title('Altura x Peso com Base na Força', fontsize=16)
plt.xlabel('Altura (cm)', fontsize=12)
plt.ylabel('Peso (kg)', fontsize=12)
plt.legend(title='Força', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# 3. Gráfico de Linhas: Quantidade de Personagens ao Longo dos Anos
plt.figure(figsize=(12, 6))
df['Year'].dropna().value_counts().sort_index().plot(kind='line', marker='o', color='green')
plt.title('Quantidade de Personagens ao Longo dos Anos', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Número de Personagens', fontsize=12)
plt.grid()
plt.show()

# 4. Gráfico de Pizza: Distribuição de Gêneros
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff'])
plt.title('Distribuição de Gêneros', fontsize=16)
plt.show()

# 5. Gráfico de Caixa (Boxplot): Altura por Gênero
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Gender', y='Height', palette='pastel')
plt.title('Distribuição de Alturas por Gênero', fontsize=16)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Altura (cm)', fontsize=12)
plt.show()

# 6. Gráfico de Correlação: Matriz de Calor
plt.figure(figsize=(10, 8))
correlation = df[['Height', 'Weight', 'Year', 'Strength']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação', fontsize=16)
plt.show()

# 7. Gráfico Interativo: Altura x Peso com Plotly
fig = px.scatter(df, x='Height', y='Weight', color='Publisher', size='Strength', hover_data=['Name'])
fig.update_layout(title='Altura x Peso Interativo', xaxis_title='Altura (cm)', yaxis_title='Peso (kg)')
fig.show()

# 8. Gráfico Interativo: Força x Ano de Primeira Aparição com Plotly
fig = px.scatter(df, x='Year', y='Strength', color='Publisher', size='Strength', 
                 hover_data=['Name', 'Gender'], 
                 labels={'Year': 'Ano de Primeira Aparição', 'Strength': 'Força'},
                 title='Força x Ano de Primeira Aparição')
fig.update_layout(
    xaxis_title='Ano de Primeira Aparição',
    yaxis_title='Força',
    showlegend=True
)

fig.show()

heroes = ['Superman', 'Aquaman', 'Black Panther', 'Batman', 'Batwoman', 'Captain Marvel', 
          'Doctor Strange', 'Flash', 'Gorilla Grodd', 'Iron Man', 'Krypto', 'Wanda Maximoff', 
          'Wonder Woman', 'Jean Grey', 'Mystique']

# Filtrar os dados para incluir apenas os personagens selecionados
df_filtered = df[df['Name'].isin(heroes)]

# Gráfico Interativo: Altura x Peso com Nome e Editora
fig = px.scatter(df_filtered, x='Height', y='Weight', color='Publisher', hover_name='Name', 
                 title='Altura x Peso dos Personagens Marvel vs DC',
                 labels={'Height': 'Altura (cm)', 'Weight': 'Peso (kg)', 'Publisher': 'Editora'},
                 color_discrete_map={'Marvel': 'blue', 'DC': 'red'})

# Exibir o gráfico
fig.show()

# Gráfico Interativo de Pizza: Distribuição de Personagens por Editora
fig = px.pie(df_filtered, names='Publisher', title='Distribuição de Personagens por Editora')
fig.show()

# Gráfico de Radar Interativo: Comparação de Força, Altura e Peso de Personagens
fig = px.line_polar(df_filtered, r='Strength', theta='Name', line_close=True, 
                    title='Comparação de Força dos Personagens')
fig.show()

# Gráfico Interativo 3D: Altura x Peso x Inteligência
fig = px.scatter_3d(df_filtered, x='Height', y='Weight', z='Intelligence', 
                    color='Publisher', hover_name='Name',
                    title='Altura, Peso e Inteligência dos Personagens')
fig.show()

# Gráfico Interativo de Boxplot: Distribuição de Altura por Editora
fig = px.box(df_filtered, x='Publisher', y='Height', points='all',
             title='Distribuição de Altura dos Personagens por Editora')
fig.show()

# Gráfico Interativo de Violin: Distribuição de Altura por Gênero
fig = px.violin(df_filtered, x='Gender', y='Height', box=True, points='all', 
                title="Distribuição de Altura por Gênero")
fig.show()