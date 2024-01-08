
# importando bibliotecas
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import nbformat

# importando dados do dataframe original
df_exportacao = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/ExpVinho.csv', sep=';')
df_exportacao

df_exportacao.shape

# visualizando as colunas de ano que serão utilizadas
df_exportacao.columns[-30:]

# **Ponto de Atenção**
# Notei que, ao importar a tabela de de exportação, os anos estão duplicados. Ao comparar a tabela acima com a tabela disponível no site da Embrapa, notei que, todos os valores que finalizam com .1, equivalem ao valor monetário, enquanto que todos os números que NÃO finalizam com `.1`, equivalem a quantidade.

# Exemplo: Linha 2 - Alemanha | 1972 == 4.168 litros exportados | 1972.1 == $ 2.630,00. Essa lógica se repete em todo o DataFrame.

# definindo quais informações do Dataframe serão utilizadas
# serão utilizadas para a análise, as colunas de 2008 a 2022, além de dados de país e ID
df_exportacao = df_exportacao[['Id', 'País', '2008', '2008.1', '2009', '2009.1', '2010', '2010.1', '2011', '2011.1',
       '2012', '2012.1', '2013', '2013.1', '2014', '2014.1', '2015', '2015.1',
       '2016', '2016.1', '2017', '2017.1', '2018', '2018.1', '2019', '2019.1',
       '2020', '2020.1', '2021', '2021.1', '2022', '2022.1']]
df_exportacao

# deletando coluna ID
df_exportacao.drop('Id', axis=1, inplace=True)

# exibindo o dataframe alterado
df_exportacao

# Criação de Tabela de Quantidade Total e Tabela de Valor Total
## Cria tabela de exportação por país
exportacao_por_pais = df_exportacao[['País', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']]
exportacao_por_pais

## cria coluna de soma total para quantidade de exportação por
exportacao_por_pais['Qtd. Total (L)'] = exportacao_por_pais ['2008']+exportacao_por_pais ['2009']\
+exportacao_por_pais ['2010']+exportacao_por_pais ['2011']+exportacao_por_pais ['2012']\
+exportacao_por_pais ['2013']+exportacao_por_pais ['2014']+exportacao_por_pais ['2015']\
+exportacao_por_pais ['2016']+exportacao_por_pais ['2017']+exportacao_por_pais ['2018']\
+exportacao_por_pais ['2019']+exportacao_por_pais ['2020']+exportacao_por_pais ['2021']\
+exportacao_por_pais ['2022']

exportacao_por_pais

# Exclui linhas de total com valor == 0
exportacao_por_pais.drop(exportacao_por_pais.loc[exportacao_por_pais['Qtd. Total (L)']==0].index, inplace=True)

# Ordenando valor da maior quantidade para a menor
exportacao_por_pais = exportacao_por_pais.sort_values(by='Qtd. Total (L)', ascending=False)
exportacao_por_pais.head()

# Cria tabela de total de exportação por país
valor_exportacao_por_pais = df_exportacao[['País', '2008.1', '2009.1', '2010.1', '2011.1', '2012.1', '2013.1', '2014.1', '2015.1', '2016.1', '2017.1', '2018.1', '2019.1', '2020.1', '2021.1', '2022.1']]
valor_exportacao_por_pais
# Cria coluna de soma MONETÁRIA total de exportação por país
valor_exportacao_por_pais['Valor Total (US$)'] = valor_exportacao_por_pais ['2008.1']+valor_exportacao_por_pais ['2009.1']\
+valor_exportacao_por_pais ['2010.1']+valor_exportacao_por_pais ['2011.1']+valor_exportacao_por_pais ['2012.1']\
+valor_exportacao_por_pais ['2013.1']+valor_exportacao_por_pais ['2014.1']+valor_exportacao_por_pais ['2015.1']\
+valor_exportacao_por_pais ['2016.1']+valor_exportacao_por_pais ['2017.1']+valor_exportacao_por_pais ['2018.1']\
+valor_exportacao_por_pais ['2019.1']+valor_exportacao_por_pais ['2020.1']+valor_exportacao_por_pais ['2021.1']\
+valor_exportacao_por_pais ['2022.1']

valor_exportacao_por_pais

# Exclui linhas com valor monetário total == 0
valor_exportacao_por_pais.drop(valor_exportacao_por_pais.loc[valor_exportacao_por_pais['Valor Total (US$)']==0].index, inplace=True)

# Ordenando valor do maior valor para o menor
valor_exportacao_por_pais = valor_exportacao_por_pais.sort_values(by='Valor Total (US$)', ascending=False)
valor_exportacao_por_pais.head()

# Unificando DataFrames
# Utilizando merge para juntar os dois DataFrames criados
df_exportacao_consolidado = pd.merge(exportacao_por_pais, valor_exportacao_por_pais, on='País', how='left')
df_exportacao_consolidado.head()

df_exportacao_consolidado

df_exportacao_consolidado.info()

df_exportacao_consolidado = df_exportacao_consolidado[['País', 'Qtd. Total (L)', 'Valor Total (US$)']]

df_exportacao_consolidado.head()
# Inclui coluna de País de Origem
df_exportacao_consolidado['País de Origem'] = df_exportacao_consolidado.index
df_exportacao_consolidado.head()

# Ordena valor por total em US$
df_exportacao_consolidado = df_exportacao_consolidado.sort_values(by='Valor Total (US$)', ascending=False)
df_exportacao_consolidado.head()

# Alterna nome da coluna de País para País de Origem
df_exportacao_consolidado.rename(columns={'País': 'País de destino'}, inplace=True)

df_exportacao_consolidado.head()

# Construindo Gráficos
## Gráfico de barras

### Cria dataframe para plotar gráfico de barras
dados_grafico_barras = df_exportacao_consolidado.head()
dados_grafico_barras = dados_grafico_barras.set_index('País de destino')
dados_grafico_barras=dados_grafico_barras.drop(columns=('País de Origem'))

# Plotando gráfico de barras
fig = px.bar(dados_grafico_barras, x=dados_grafico_barras.index, y=dados_grafico_barras.columns, barmode='group', template='plotly_white')
fig.update_layout(title='Quantidade e valor total exportado (2008 a 2022)', width = 700)
fig.update_xaxes(title_text="Ano")
fig.update_yaxes(title_text="Valor")
fig.show()

df_exportacao_consolidado.info()

# Gráfico Total (L) Exportado Por País - Top 10
grafico_quantidade = px.bar(df_exportacao_consolidado.head(10), 
                                x='País de destino', 
                                y='Qtd. Total (L)', 
                                template='plotly_white', 
                                title='Total Exportado', 
                                width=800
                            )

grafico_quantidade.show()

# Total ($) Exportado US$ Por País - Top 10
grafico_valor = px.bar(df_exportacao_consolidado.head(10),
                        x='País de destino',
                        y='Valor Total (US$)',
                        template='plotly_white',
                        title='Total Exportado',
                        width=800
                    )

grafico_valor.show()

df_exportacao_consolidado.describe()

# Cria dataframe para criação de gráfico de linha de evolução
dados_grafico_linha_qtd = exportacao_por_pais.set_index('País')
dados_grafico_linha_qtd = dados_grafico_linha_qtd.drop('Qtd. Total (L)', axis=1)
dados_grafico_linha_qtd.head()

# Transpondo tabela
dado_qtd=dados_grafico_linha_qtd.head()
dado_qtd = dado_qtd.T
dado_qtd.head()

# Cria gráfio de evolução de exportação para Russia
fig = px.line(dado_qtd,
                x=dado_qtd.index,
                y='Rússia',
                markers=True,
                template='plotly_white',
                title='Evolução de exportação para Rússia',
                width=700
            )

fig.show()

# Cria gráfio de evolução de exportação Paraguai
fig = px.line(dado_qtd, x=dado_qtd.index,
                y='Paraguai',
                markers=True,
                template='plotly_white',
                title='Evolução de exportação para o Paraguai',
                width=700
            )

fig.show()

# Cria gráfio de evolução de exportação Estados Unidos
fig = px.line(dado_qtd,
                x=dado_qtd.index,
                y='Estados Unidos',
                markers=True,
                template='plotly_white',
                title='Evolução de exportação para os Estados Unidos',
                width=700
            )

fig.show()

# Evolução de exportação para os 5 maiores compradores
fig = px.line(dado_qtd,
                x=dado_qtd.index,
                y=dado_qtd.columns, 
                markers=True,
                template='plotly_white',
                title='Evolução de exportação para os 5 maiores compradores (em L)',
                width=700
            )

fig.show()

# Cria dataframe desenvolvimento do gráfico de linha - para valores
dados_grafico_linha_valor = valor_exportacao_por_pais.set_index('País')
dados_grafico_linha_valor = dados_grafico_linha_valor.drop('Valor Total (US$)', axis=1)
dados_grafico_linha_valor.head()

# Atualiza os nomes de colunas
dados_grafico_linha_valor.rename(columns={'2008.1': '2008'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2009.1': '2009'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2010.1': '2010'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2011.1': '2011'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2012.1': '2012'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2013.1': '2013'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2014.1': '2014'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2015.1': '2015'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2016.1': '2016'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2017.1': '2017'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2018.1': '2018'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2019.1': '2019'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2020.1': '2020'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2021.1': '2021'}, inplace=True)
dados_grafico_linha_valor.rename(columns={'2022.1': '2022'}, inplace=True)

dados_grafico_linha_valor.head()

# Transpondo tabela
dado_valor = dados_grafico_linha_valor.head()
dado_valor = dado_valor.T
dado_valor.head()

# Evolução de valores paraguai
fig = px.line(dado_valor, 
                x=dado_valor.index, 
                y='Paraguai', 
                markers=True,
                template='plotly_white', 
                title='Evolução de exportação para o Paraguai (em US$)', width=700
            )

fig.show()

# Evolução de valores estados unidos
fig = px.line(dado_valor, 
                x=dado_valor.index, 
                y='Estados Unidos', 
                markers=True,
                template='plotly_white', 
                title='Evolução de exportação para os Estados Unidos (em US$)', 
                width=700
            )

fig.show()

# Evolução de valores para o top 5 compradores
fig = px.line(dado_valor,
                x=dado_valor.index, 
                y= dado_valor.columns, 
                markers=True, 
                template='plotly_white', 
                title='Evolução de exportação para os 5 maiores compradores (em US$)', 
                width=700
            )

fig.show()

# Cria dataframe com valores de quantidade e valor por país
dados_valores_totais_pais = df_exportacao_consolidado.drop(columns=('País de Origem'))
dados_valores_totais_pais.head()

# Cria dataframe com quantidade exportada total por ano
dados_qtd_total_anual = dados_grafico_linha_qtd.sum()
dados_qtd_total_anual = pd.DataFrame(dados_qtd_total_anual)
dados_qtd_total_anual.head()
dados1_qtd_total_anual = dados_qtd_total_anual.reset_index()
dados1_qtd_total_anual.index.rename('novoIndex', inplace=True)
dados1_qtd_total_anual.head()

# Cria dataframe com quantidade exportada total por ano
dados_valor_total_anual = dados_grafico_linha_valor.sum()
dados_valor_total_anual = pd.DataFrame(dados_valor_total_anual)
dados_valor_total_anual.head()
dados2_valor_total_anual = dados_valor_total_anual.reset_index()
dados2_valor_total_anual.index.rename('novoIndex', inplace=True)
dados2_valor_total_anual.head()

# Cria dataframe com valores totais de exportação por ano(quantidade e valores)
dados_totais_qtd_valor = pd.merge(dados1_qtd_total_anual, dados2_valor_total_anual, on='novoIndex', how='left')
dados_totais_qtd_valor = dados_totais_qtd_valor.drop('index_y', axis=1)
dados_totais_qtd_valor.head()

# Organizando novo dataframe para plotar os gráficos
dados_totais_qtd_valor.rename(columns={'index_x' : 'Ano', '0_x' : 'Quantidade', '0_y' : 'Valor'}, inplace=True)
dados_totais_qtd_valor = dados_totais_qtd_valor
dados_totais_qtd_valor = dados_totais_qtd_valor.set_index('Ano')

dados_totais_qtd_valor

# Evolução da quantidade e valor de exportação no período de 2008 à 2022
fig = px.line(dados_totais_qtd_valor,
                x=dados_totais_qtd_valor.index,
                y=dados_totais_qtd_valor.columns,
                markers=True,
                template='plotly_white',
                title='Evolução de exportação no período de 2008 à 2022',
)

fig.show()

# Evolução dos valores de exportação no período de 2008 à 2022
fig = px.bar(dados_totais_qtd_valor,
                y=dados_totais_qtd_valor['Valor'], template='plotly_white',
                title= 'Valores de exportação ano a ano',
                width=700                
)

fig.show()

dados_totais_qtd_valor

# Evolução da quantidade de exportação no período de 2008 à 2022
fig = px.bar(dados_totais_qtd_valor,
                x = dados_totais_qtd_valor.index,
                y = dados_totais_qtd_valor.columns,
                barmode='group',
                template='plotly_white',
)
fig.update_layout(title='Quantidade x Valor total de exportação entre 2008 e 2022', width=700)
fig.update_xaxes(title_text='Ano')
fig.update_yaxes(title_text='Valor')

fig.show()

# Evolução da quantidade de exportação no período de 2008 à 2022
fig=px.scatter(df_exportacao_consolidado,
                x='Qtd. Total (L)',
                y='Valor Total (US$)',
                log_x = True,
                log_y = True,
                width=700,
                opacity = 0.7,
                template='plotly_white'
)   
fig.update_traces(marker = dict(size=8, line=dict(width=1)),
                    selector=dict(mode='markers')
)
fig.update_layout(title='Dispersão das exportações no período')
fig.update_xaxes(title_text='Quantidade')
fig.update_yaxes(title_text='Valor')

fig.show()


# Exportando DataFrames para utilização no Streamlit

## df_exportacao_consolidado.to_csv('bases/df_exportacao_consolidado.csv')
## df_exportacao_consolidado

## dado_valor.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadoValor.csv')
## dado_valor

## dado_qtd.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dado_qtd.csv')
## dado_qtd

## dados1_qtd_total_anual.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dados1QtdTotalAnual.csv')
## dados1_qtd_total_anual

## dados2_valor_total_anual.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dados2ValorTotalAnual.csv')
## dados2_valor_total_anual

## dados_graficos_barras.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosGraficoBarras.csv')
## dados_graficos_barras

## dados_graficos_linha_qtd.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosGraficoLinhaQtd.csv')
## dados_graficos_linha_qtd

## dados_grafico_linha_valor.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosGraficoLinhaValor.csv')
## dados_grafico_linha_valor

## dados_totais_qtd_valor.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosTotaisQtdValor.csv')
## dados_totais_qtd_valor

## dados_valores_totais_pais.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosValoresTotaisPais.csv')
## dados_valores_totais_pais

## exportacao_por_pais.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/exportacaoPorPais.csv')
## exportacao_por_pais

## valor_exportacao_por_pais.to_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/valorExportacaoPorPais.csv')
## valor_exportacao_por_pais