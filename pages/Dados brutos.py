import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dados brutos | TechChallenge FIAP :wine_glass:', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png')

# tabela de dado que será utilizada na exibição da aplicação
st.title('Dados brutos')

st.markdown('## Dicionário de Dados :nerd_face:')
st.markdown('''Diversas transformações e DataFrames foram criados no decorrer do projeto para que fosse possível as análises apresentadas na página de Dashboard.'
            
Para que que as informações fiquem organizadas e seja possível mapear o que feito, segue abaixo um "dicionário" com os DataFrames criados à partir da base de dados original.

Não é um tópico de interesse de negócio mas, está voltado para equipes técnicas do cliente que, eventualmente, precisem entender como a construção da aplicação foi feita. Além disso, podem utilizar essas informações para novas análises e cruzamentos, para explorar ***insights*** que não foram abordados nesta análise ou explorar novas hipóteses de negócio.
''')

st.markdown('''
###### 1. `df_exportacao`
DataFrame criado à partir da base de dados original. Algumas limpezas e manipulações foram feitas para que, no final, tivéssemos um DataFrame com as seguintes colunas:
                      
- Colunas País: com todos os países destino de exportação
- Colunas 2008 à 2022: cada ano possui o registro de valores de exportação. Da forma como a base de dados veio, há duas colunas de ano para cada ano; uma coluna contém o **valor monetário** em dólar americado (US$) e a outra coluna contém a **quantidade** de produto exportado em litros.
''')

df_exportacao = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dfexportacao.csv')
st.dataframe(df_exportacao, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 2. `exportacao_por_pais`
Cria um DataFrame com a **quantidade em litros** exportada. Foram excluídas as colunas de valor monetário e criada uma coluna final com a soma total de litros exportados por país:

- Colunas País: com todos os países destino de exportação
- Colunas 2008 à 2022: com o registro de quantidade de litros exportados por ano.
- Coluna Qtd. Total (L): com a soma total de litros exportados por país.
''')

exportacao_por_pais = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/exportacaoPorPais.csv')
st.dataframe(exportacao_por_pais, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 3. `valor_exportacao_por_pais`
Cria um DataFrame com o **valor monetário** exportado. Foram excluídas as colunas de quantidade em litros e criada uma coluna final com a soma total de valor monetário exportado por país:

- Colunas País: com todos os países destino de exportação
- Colunas 2008 à 2022: com o registro de valor monetário exportado por ano.
- Coluna Valor Total (US$): com a soma total de valor monetário exportado por país.
''')

valor_exportacao_por_pais = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/valorExportacaoPorPais.csv')
st.dataframe(valor_exportacao_por_pais, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 4. `df_exportacao_consolidado`
Cria um DataFrame, atravé do `mege` dos DataFrames `exportacao_por_pais` e `valor_exportacao_por_pais`, incluindo também uma coluna de País de Origem (Brasil) e renomeando a primeira coluna do DataFrame de **País** > **País de destino**, com as seguintes colunas:

- Coluna País de destino: com todos os países destino de exportação
- Coluna Qtd. Total (L): com a quantidade total de litros exportados por país
- Coluna Valor Total (US$): com o valor monetário total de exportação por país
- Coluna País de Origem: ainda não com o país correto mas, já com o espaço para inclusão dessa informação.
''')

df_exportacao_consolidado = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dfExportacaoConsolidado.csv')
st.dataframe(df_exportacao_consolidado, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 5. `dados_grafico_barras`
DataFrame criado para a construção de gráficos de barras. À partir do DataFrame `df_exportacao_consolidado`, foi excluída a coluna **País de Origem**, ficando com as seguintes colunas:

- Coluna País de destino: com todos os países destino de exportação
- Coluna Qtd. Total (L): com a quantidade total de litros exportados por país
- Coluna Valor Total (US$): com o valor monetário total de exportação por país
''')

dados_grafico_barras = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosGraficoBarras.csv')
st.dataframe(dados_grafico_barras, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 6. `dados_grafico_linha_qtd`
DataFrame criado para a construção de gráfico de linhas, para analisar a evolução da quantidade exportada na linha do tempo. Este DataFrame ficou com as seguintes colunas:

- Coluna País: com todos os países destino de exportação
- Colunas 2008 à 2022: com o registro de quantidade de litros exportados por ano, de cada país
''')

dados_grafico_linha_qtd = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosGraficoLinhaQtd.csv')
st.dataframe(dados_grafico_linha_qtd, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 7. `dado_qtd`
DataFrame criado à partir do df `dados_grafico_linha_qtd` e transposto para que as colunas de ano fiquem na linha e países em coluna.
''')

dado_qtd = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dado_qtd.csv')
st.dataframe(dado_qtd, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 8. `dados_grafico_linha_valor`
DataFrame ciado para a construção de gráficos de linhas, para analisar a evolução monetária nas transações de exportação. Este DataFrame ficou com as seguintes colunas:

- Coluna País: com todos os países destino de exportação
- Colunas 2008 à 2022: com o registro de valor monetário exportado por ano, de cada país
''')

dados_grafico_linha_valor = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosGraficoLinhaValor.csv')
st.dataframe(dados_grafico_linha_valor, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 9. `dado_valor`
DataFrame criado à partir do df `dados_grafico_linha_valor` e transposto para que as colunas de ano fiquem na linha e países em coluna.
''')

dado_valor = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadoValor.csv')
st.dataframe(dado_valor, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 10. `dados_valores_totais_pais`
DataFrame criado para manipulação de informações que vão ser usadas na criação de mais dois Dataframes: `dados1_qtd_total_anual` e `dados2_valor_total_anual`.
''')

dados_valores_totais_pais = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosValoresTotaisPais.csv')
st.dataframe(dados_valores_totais_pais, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 11. `dados1_qtd_total_anual`
DataFrame criado, contendo apenas duas colunas: **index** contendo todos os anos (de 2008 à 2022) e **0** contendo a soma total de litros exportados em cada ano.
''')

dados1_qtd_total_anual = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dados1QtdTotalAnual.csv')
st.dataframe(dados1_qtd_total_anual, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 12. `dados2_valor_total_anual`
DataFrame criado, contendo apenas duas colunas: **index** contendo todos os anos (de 2008 à 2022) e **0** contendo a soma total de valor monetário exportado em cada ano.
''')

dados2_valor_total_anual = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dados2ValorTotalAnual.csv')
st.dataframe(dados2_valor_total_anual, use_container_width=True)

st.markdown('---')

st.markdown('''
###### 13. `dados_totais_qtd_valor`
DataFrame criado à partir do `merge` dos DataFrames `dados1_qtd_total_anual` e `dados2_valor_total_anual`, contendo as seguintes colunas:

- Coluna Ano: com todos os anos (de 2008 à 2022)
- Coluna Quantidade: com a soma total de litros exportados em cada ano
- Coluna Valor: com a soma total de valor monetário exportado em cada ano

''')

dados_totais_qtd_valor = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dadosTotaisQtdValor.csv')
st.dataframe(dados_totais_qtd_valor, use_container_width=True)