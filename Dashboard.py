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