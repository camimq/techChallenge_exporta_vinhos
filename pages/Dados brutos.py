import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dados brutos | TechChallenge FIAP :wine_glass:', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png', layout='wide')

# tabela de dado que será utilizada na exibição da aplicação
st.title('Dados brutos')

st.markdown('## Dicionário de Dados :nerd_face:')
st.markdown('Todos os DataFrames criados no decorrer das análises estão dispostos nesta página')

df_exportacao_consolidado = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dfExporta.csv')
st.dataframe(df_exportacao_consolidado, use_container_width=True)