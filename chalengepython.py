# -*- coding: utf-8 -*-
"""ChalengePython (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10khvcX_sioV8LmS3YQ3tPSW8DHcnu311

### Importação dos dados
"""

import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja.head()

"""#1. Análise do faturamento

"""

# 1. FATURAMENTO POR LOJA

#Calculando o faturamento total de cada loja
faturamento_loja1 = loja['Preço'].sum()
faturamento_loja2 = loja2['Preço'].sum()
faturamento_loja3 = loja3['Preço'].sum()
faturamento_loja4 = loja4['Preço'].sum()

# EXIBIR RESULTADO
print("1. FATURAMENTO POR LOJA\n")
print(f"Faturamento Loja 1: R${faturamento_loja1:,.0f}")
print(f"Faturamento Loja 2: R${faturamento_loja2:,.0f}")
print(f"Faturamento Loja 3: R${faturamento_loja3:,.0f}")
print(f"Faturamento Loja 4: R${faturamento_loja4:,.0f}\n")

# 2.FATURAMENTO TOTAL REDE

faturamento_total = faturamento_loja1 + faturamento_loja2 + faturamento_loja3 + faturamento_loja4
faturamento_medio = faturamento_total / 4

#EXIBIR RESULTADO
print("2. FATURAMENTO POR LOJA\n")
print(f"Faturamento Total: R${faturamento_total:,.0f}\n")
print(f"Faturamento Medio: R${faturamento_medio:,.0f}\n")

# 3. RANKING DE MELHORES VENDAS

print("3. RANKING DE MELHORES VENDAS:\n")

import pandas as pd

dados = pd.Series({
    'Loja 1': faturamento_loja1,
    'Loja 2': faturamento_loja2,
    'Loja 3': faturamento_loja3,
    'Loja 4': faturamento_loja4
})

ranking = dados.rank(ascending=False, method='min')  # 1 = maior valor
print(ranking)

#4. VENDA POR UF

print("\n4. VENDA POR UF\n")
print("Faturamento por UF de cada loja por regiao (R$/%):\n")
#print(faturamento_uf_loja1)

#Dicionario de regioes
uf_regiao = {
    'AC': 'Norte',
    'AL': 'Nordeste',
    'AP': 'Norte',
    'AM': 'Norte',
    'BA': 'Nordeste',
    'CE': 'Nordeste',
    'DF': 'Centro-Oeste',
    'ES': 'Sudeste',
    'GO': 'Centro-Oeste',
    'MA': 'Nordeste',
    'MT': 'Centro-Oeste',
    'MS': 'Centro-Oeste',
    'MG': 'Sudeste',
    'PA': 'Norte',
    'PB': 'Nordeste',
    'PR': 'Sul',
    'PE': 'Nordeste',
    'PI': 'Nordeste',
    'RJ': 'Sudeste',
    'RN': 'Nordeste',
    'RS': 'Sul',
    'RO': 'Norte',
    'RR': 'Norte',
    'SC': 'Sul',
    'SP': 'Sudeste',
    'SE': 'Nordeste',
    'TO': 'Norte'
}

# Conversao UF para Regiao
loja['Região'] = loja['Local da compra'].map(uf_regiao)
loja2['Região'] = loja2['Local da compra'].map(uf_regiao)
loja3['Região'] = loja3['Local da compra'].map(uf_regiao)
loja4['Região'] = loja4['Local da compra'].map(uf_regiao)

#Calculo do faturamento total de cada loja por UF
faturamento_regiao_loja1 = loja.groupby('Região')['Preço'].sum()
faturamento_regiao_loja2 = loja2.groupby('Região')['Preço'].sum()
faturamento_regiao_loja3 = loja3.groupby('Região')['Preço'].sum()
faturamento_regiao_loja4 = loja4.groupby('Região')['Preço'].sum()

faturamento_regiao_total = faturamento_regiao_loja1 + faturamento_regiao_loja2 + faturamento_regiao_loja3 + faturamento_regiao_loja4

#Faturamento total da loja (mencionado no item 1 #CODIGO faturamento_loja1 = loja['Preço'].sum())
percentual_regiao_loja1 = (faturamento_regiao_loja1 / faturamento_loja1) * 100
percentual_regiao_loja2 = (faturamento_regiao_loja2 / faturamento_loja2) * 100
percentual_regiao_loja3 = (faturamento_regiao_loja3 / faturamento_loja3) * 100
percentual_regiao_loja4 = (faturamento_regiao_loja4 / faturamento_loja4) * 100

percentual_regiao_total = (faturamento_regiao_total / faturamento_total) * 100

#EXIBIR RESULTADO

# Exibir como tabela com valores em R$ e %
print("Faturamento loja 1:\n")

df_percentual_loja1 = pd.DataFrame({
    'Faturamento (R$)': faturamento_regiao_loja1,
    'Participação (%)': percentual_regiao_loja1
})
print(df_percentual_loja1.round(2))

print("\nFaturamento loja 2:\n")
df_percentual_loja2 = pd.DataFrame({
    'Faturamento (R$)': faturamento_regiao_loja2,
    'Participação (%)': percentual_regiao_loja2
})
print(df_percentual_loja2.round(2))

print("\nFaturamento loja 3:\n")
df_percentual_loja3 = pd.DataFrame({
    'Faturamento (R$)': faturamento_regiao_loja3,
    'Participação (%)': percentual_regiao_loja3
})
print(df_percentual_loja3.round(2))

print("\nFaturamento loja 4:\n")
df_percentual_loja4 = pd.DataFrame({
    'Faturamento (R$)': faturamento_regiao_loja4,
    'Participação (%)': percentual_regiao_loja4
})
print(df_percentual_loja4.round(2))

print("\nFaturamento total:\n")
df_percentual_total = pd.DataFrame({
    'Faturamento (R$)': faturamento_regiao_total,
    'Participação (%)': percentual_regiao_total
})
print(df_percentual_total.round(2))

#GRAFICO VENDA POR REGIAO

import matplotlib.pyplot as plt

# Gráfico de pizza
plt.figure(figsize=(4, 4))
plt.pie(
    faturamento_regiao_total,                     # Valores
    labels=faturamento_regiao_total.index,        # Rótulos (regiões)
    autopct='%1.1f%%',                            # Mostrar % em cada fatia
    startangle=90,                                # Começar o gráfico em 90° (estética)
    colors=plt.cm.Pastel1.colors                  # Cores suaves opcionais
)

plt.title('Participação no Faturamento por Região')
plt.axis('equal')  # Deixa o gráfico redondo
plt.show()

"""# 2. Vendas por Categoria

"""

# 1. ANALISE GERAL - VENDAS POR CATEGORIAS

#VENDA POR CATEGORIA
todas_categorias = pd.concat([
    loja['Categoria do Produto'],
    loja2['Categoria do Produto'],
    loja3['Categoria do Produto'],
    loja4['Categoria do Produto']
])

categorias_unicas = todas_categorias.unique()
categorias_unicas_ordenadas = sorted(categorias_unicas)

# 2. FATURAMENTO POR CATEGORIA EM CADA LOJA

faturamento_categoria_loja1 = loja.groupby('Categoria do Produto')['Preço'].sum()
faturamento_categoria_loja2 = loja2.groupby('Categoria do Produto')['Preço'].sum()
faturamento_categoria_loja3 = loja3.groupby('Categoria do Produto')['Preço'].sum()
faturamento_categoria_loja4 = loja4.groupby('Categoria do Produto')['Preço'].sum()

#double check valores totais:
faturamento_total_todas_lojas = sum(faturamento_categoria_loja1) + sum(faturamento_categoria_loja2) + sum(faturamento_categoria_loja3) + sum(faturamento_categoria_loja4)
#print(faturamento_total_todas_lojas)

#concatenar categorias x vendas de todas as lojas
faturamento_categoria_total = faturamento_categoria_loja1 + faturamento_categoria_loja2 + faturamento_categoria_loja3 + faturamento_categoria_loja4
df_faturamento_categoria_total = faturamento_categoria_total.fillna(0) #Substituir NaNs por 0, caso uma loja não tenha vendido uma categoria específica

print(df_faturamento_categoria_total)

#2.1 VENDA TOTAL POR CATEGORIA - COMPARATIVO ENTRE LOJAS
df_comparativo = pd.DataFrame({
    'Loja 1': faturamento_categoria_loja1,
    'Loja 2': faturamento_categoria_loja2,
    'Loja 3': faturamento_categoria_loja3,
    'Loja 4': faturamento_categoria_loja4
})
df_comparativo = df_comparativo.fillna(0) # Substituir NaNs por 0, caso uma loja não tenha vendido uma categoria específica

# EXIBIR RESULTADOS
# 1. FATURAMENTO POR LOJA

print("1. VENDA POR CATEGORIA\n ")
print("Faturamento por Categoria de Produto (Todas as Lojas):\n")

import matplotlib.pyplot as plt

bars = plt.bar(categorias_unicas_ordenadas, df_faturamento_categoria_total)
plt.title("Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.tight_layout()

# Adicionar os rótulos de valor acima de cada barra
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.2f}', ha='center', va='bottom', fontsize=9)
plt.show()

#EXIBIR RESULTADOS
#2. VENDA TOTAL POR CATEGORIA - COMPARATIVO ENTRE LOJAS

print('2. VENDA TOTAL POR CATEGORIA - COMPARATIVO ENTRE LOJAS\n')
print("\nFaturamento por Categoria de Produto (Comparativo entre Lojas):\n")
print(df_comparativo)

#grafico para visualizacao de faturamento por categoria por loja
import matplotlib.pyplot as plt

# Plot
ax = df_comparativo.plot(kind='bar', figsize=(6, 5))
plt.title("Faturamento por Categoria - Comparativo entre Lojas")
plt.xlabel("Categoria do Produto")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.legend(title='Lojas')
plt.tight_layout()
plt.show()

"""# 3. Média de Avaliação das Lojas"""

#Calculando a avaliacao media das lojas

avaliacao_loja1 = loja['Avaliação da compra'].sum()/len(loja)
avaliacao_loja2 = loja2['Avaliação da compra'].sum()/len(loja2)
avaliacao_loja3 = loja3['Avaliação da compra'].sum()/len(loja3)
avaliacao_loja4 = loja4['Avaliação da compra'].sum()/len(loja4)

avaliacoes = [avaliacao_loja1, avaliacao_loja2, avaliacao_loja3, avaliacao_loja4]
minimo_aval = min(avaliacoes)
maximo_aval = max(avaliacoes)

print("A avalicao media de cada loja corresponde a:\n")
print(f"Loja 1: {avaliacao_loja1:,.2f}")
print(f"Loja 2: {avaliacao_loja2:,.2f}")
print(f"Loja 3: {avaliacao_loja3:,.2f}")
print(f"Loja 4: {avaliacao_loja4:,.2f}\n")

print(f"Sendo o menor resultado {minimo_aval:,.2f} e o maior resultado: {maximo_aval:,.2f}")



"""# 4. Produtos Mais e Menos Vendidos"""

# Venda de cada produto por loja - Visualizacao por loja
produtos_vendidos_loja1 = loja.groupby('Produto').agg(quant_vendida=('Produto', 'count'), faturamento=('Preço', 'sum')).sort_values(by='quant_vendida', ascending=False)
produtos_vendidos_loja2 = loja2.groupby('Produto').agg(quant_vendida=('Produto', 'count'), faturamento=('Preço', 'sum')).sort_values(by='quant_vendida', ascending=False)
produtos_vendidos_loja3 = loja3.groupby('Produto').agg(quant_vendida=('Produto', 'count'), faturamento=('Preço', 'sum')).sort_values(by='quant_vendida', ascending=False)
produtos_vendidos_loja4 = loja4.groupby('Produto').agg(quant_vendida=('Produto', 'count'), faturamento=('Preço', 'sum')).sort_values(by='quant_vendida', ascending=False)

mais_vendido_loja1 = produtos_vendidos_loja1['quant_vendida'].idxmax()
menos_vendido_loja1 = produtos_vendidos_loja1['quant_vendida'].idxmin()
quantidade_mais_vendido_loja1 = produtos_vendidos_loja1.loc[mais_vendido_loja1, 'quant_vendida']
quantidade_menos_vendido_loja1 = produtos_vendidos_loja1.loc[menos_vendido_loja1, 'quant_vendida']

mais_vendido_loja2 = produtos_vendidos_loja2['quant_vendida'].idxmax()
menos_vendido_loja2 = produtos_vendidos_loja2['quant_vendida'].idxmin()
quantidade_mais_vendido_loja2 = produtos_vendidos_loja2.loc[mais_vendido_loja2, 'quant_vendida']
quantidade_menos_vendido_loja2 = produtos_vendidos_loja2.loc[menos_vendido_loja2, 'quant_vendida']

mais_vendido_loja3 = produtos_vendidos_loja3['quant_vendida'].idxmax()
menos_vendido_loja3 = produtos_vendidos_loja3['quant_vendida'].idxmin()
quantidade_mais_vendido_loja3 = produtos_vendidos_loja3.loc[mais_vendido_loja3, 'quant_vendida']
quantidade_menos_vendido_loja3 = produtos_vendidos_loja3.loc[menos_vendido_loja3, 'quant_vendida']

mais_vendido_loja4 = produtos_vendidos_loja4['quant_vendida'].idxmax()
menos_vendido_loja4 = produtos_vendidos_loja4['quant_vendida'].idxmin()
quantidade_mais_vendido_loja4 = produtos_vendidos_loja4.loc[mais_vendido_loja4, 'quant_vendida']
quantidade_menos_vendido_loja4 = produtos_vendidos_loja4.loc[menos_vendido_loja4, 'quant_vendida']


#ANALISE MONTANTE DE LOJAS

produtos_todas_lojas = pd.concat([
    loja['Produto'],
    loja2['Produto'],
    loja3['Produto'],
    loja4['Produto']
])

# Retorna tupla com (nome_produto, qtd)
mais_vendido = quant_produtos_todas_lojas[quant_produtos_todas_lojas == quant_produtos_todas_lojas.max()]
menos_vendido = quant_produtos_todas_lojas[quant_produtos_todas_lojas == quant_produtos_todas_lojas.min()]

# Exibir

#RESULTADOS

print('Analise detalhada por loja\n')

print(f"O produto mais vendido na loja 1 foi {mais_vendido_loja1.upper()} com {quantidade_mais_vendido_loja1} unidades vendidas, enquanto o produto menos foi {menos_vendido_loja1.upper()} com {quantidade_menos_vendido_loja1} unidades vendidas")
print(f"O produto mais vendido na loja 2 foi {mais_vendido_loja2.upper()} com {quantidade_mais_vendido_loja2} unidades vendidas, enquanto o produto menos foi {menos_vendido_loja2.upper()} com {quantidade_menos_vendido_loja2} unidades vendidas")
print(f"O produto mais vendido na loja 3 foi {mais_vendido_loja3.upper()} com {quantidade_mais_vendido_loja3} unidades vendidas, enquanto o produto menos foi {menos_vendido_loja3.upper()} com {quantidade_menos_vendido_loja3} unidades vendidas")
print(f"O produto mais vendido na loja 4 foi {mais_vendido_loja4.upper()} com {quantidade_mais_vendido_loja4} unidades vendidas, enquanto o produto menos foi {menos_vendido_loja4.upper()} com {quantidade_menos_vendido_loja4} unidades vendidas\n")

print('Analise geral (todas as lojas)\n')

print("O(s) Produto(s) mais vendido(s) considerando-se toda a rede de lojas:")
print(mais_vendido)

print("\nProduto(s) menos vendido(s):")
print(menos_vendido)



"""# 5. Frete Médio por Loja

"""

#Calculando o valor medio media de frete por loja

frete_loja1 = loja['Frete'].sum()/len(loja)
frete_loja2 = loja2['Frete'].sum()/len(loja2)
frete_loja3 = loja3['Frete'].sum()/len(loja3)
frete_loja4 = loja4['Frete'].sum()/len(loja4)


print("O valor medio de frete cobrado por cada loja corresponde a:\n")
print(f"Loja 1: R${frete_loja1:,.2f}")
print(f"Loja 2: R${frete_loja2:,.2f}")
print(f"Loja 3: R${frete_loja3:,.2f}")
print(f"Loja 4: R${frete_loja4:,.2f}\n")

"""# 6. Desafio proposto

Durante este desafio, **você irá ajudar o Senhor João a decidir qual loja da sua rede Alura Store vender** para iniciar um novo empreendimento. Para isso, você analisará dados de vendas, desempenho e avaliações das 4 lojas fictícias da Alura Store.

O objetivo é identificar a **loja com menor eficiência** e apresentar uma recomendação final baseada nos dados.

**O que você vai praticar:**

1.   Carregar e manipular dados CSV com a biblioteca Pandas .
2.   Criar visualizações de dados com biblioteca Matplotlib.
3.   Analisar métricas como faturamento, avaliações e desempenho de vendas.

**Requisitos:**

* **Analisar os dados das lojas:**

Você deve avaliar informações como faturamento, categorias mais vendidas, avaliações dos clientes, produtos mais vendidos e frete médio.

* **Criar gráficos para visualização:**

Decida quais tipos de gráficos usar para apresentar os resultados de maneira clara e visual.

Mínimo de 3 gráficos diferentes, que podem incluir gráficos de barras, pizza, dispersão, entre outros.

* **Apresentar uma recomendação:**

Após as análises, escreva um texto explicando qual loja o Senhor João deve vender e por quê, com base nos dados apresentados.

# 7. Análise Consolidada

Com base na análise dos indicadores de desempenho das quatro lojas da rede, **a Loja 4 se destaca negativamente** em diversos aspectos críticos, tornando-se a principal candidata à venda. Para reestruturação e investimento da rede Alura Store, seguem os principais pontos que justificam essa decisão:

### **Desempenho Financeiro Inferior**

- O faturamento da Loja 4 foi de R\$ 1.384.498, **abaixo da média da rede** (R\$ 1.467.873).
- É a loja com **menor faturamento absoluto**, atrás inclusive da Loja 3, que ainda ficou levemente abaixo da média.
- A contribuição da Loja 4 para o faturamento total é a mais baixa entre todas as unidades.

### **Desempenho por Categoria de Produto**

- A Loja 4 apresentou resultados abaixo da média em quase todas as categorias.
- Desempenho especialmente fraco nas **vendas de eletrodomésticos**, um dos principais pilares da rede.
- Apresentou apenas faturamento mediano em eletrônicos e móveis, categorias essenciais para a performance da empresa.

### **Desempenho Geográfico Limitado**

- **A Região Sudeste é responsável pela maior parte do faturamento da rede**, com R\$ 3.988.869 em vendas, representando **67,94% do total da rede**.
- A Loja 4 não se destaca em nenhuma região específica, não aproveitando o potencial geográfico da rede.

### **Avaliação de Clientes**

- A Loja 4 possui uma avaliação inferior a loja 3, superando apenas a Loja 1 — que, por outro lado, apresenta o melhor desempenho comercial da rede.
- A baixa nota impacta diretamente na percepção da marca, fidelização e potencial de crescimento.

### **Custo Logístico e Frete**

- Apesar de apresentar um dos menores custos com frete, este não se converte em vantagem competitiva.
- O frete baixo não compensa os fracos resultados em vendas e avaliação, o que indica baixo volume operacional e menor eficiência.

## **Conclusão**

Com baixo faturamento, desempenho fraco por categoria, avaliação ruim e sem uma base geográfica forte, a Loja 4 representa um gargalo estratégico para a rede. Os dados indicam que seus resultados não justificam sua manutenção ativa, e sua venda poderia:

- Reduzir custos operacionais;
- Reforçar o capital de giro;
- Permitir a concentração de esforços nas unidades mais rentáveis.

**Portanto, recomenda-se a venda ou reestruturação completa da Loja 4.**
"""