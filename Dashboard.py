import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Home | TechChallenge FIAP :wine_glass:', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png', layout='wide')
aba1, aba2, aba3, aba4, aba5, aba6, aba7, aba8 = st.tabs(['Histórico', 'Produção', 'Exportação', 'Comercialização', 'Importação', 'Influências', 'Consumo', 'Conclusão'])

with aba1:
    st.markdown('## Histórico')
with aba2:
    st.markdown('## Produção')
with aba3:
    st.markdown('## Exportação')
    st.markdown('''
                
                                Criar um relatório inicial que será apresentado a um grupo de investidores e acionistas, explicando a quantidade de vinhos exportados e os fatores externos que podem vir a surgir e que interferem nas análises:

                1. Dados climáticos
                2. Dados demográficos
                3. Dados econômicos
                4. Dados de avaliações de vinhos     
                        
                Além disso, é esperado que seja construída uma tabela que contenha as seguintes informações:
                            
                a. País de origem (Brasil)

                b. País de destino

                c. Quantidade em litros de vinho exportado

                d. Valores em dólar americano (US$)

                ## Objetivo

                Dizer o montante de venda de exportação nos **últimos 15 anos**, separando a análise por país e trazendo quais as prospecções futuras e possíveis ações para uma melhoria nas exportações, através da construção de gráficos que passem a ideia central para que os acionistas e investidores possam seguir em frente com suas ações.  
                ### Tabela de Exportação
''')
    df_exportacao_consolidado = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dfExporta.csv')
    df_exportacao_consolidado['País de Origem'] = 'Brasil'
    st.dataframe(df_exportacao_consolidado, use_container_width=True)
with aba4:
    st.markdown('## Comercialização')
with aba5:
    st.markdown('## Importação')
with aba6:
    st.markdown('## Influências')
with aba7:
    st.markdown('## Consumo')
with aba8:
    st.markdown('## Conclusão')