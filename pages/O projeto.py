import streamlit as st

# Layout da aplicação
col1, col2 = st.columns(2)
with col1:
    st.title('O Projeto')
    st.markdown('''
    O objetivo do projeto, é entregar a análise de um conjunto de dados disponível no [site da Embrapa](https://www.cnpuv.embrapa.br/vitibrazil/index.php?opcao=opt_02) e que contém informações sobre a quantidade de uvas processadas, produção e comercialização de vinhos, sucos e derivados, proveninentes do Estado do Rio Grande do Sul e que, ainda de acordo com a **Embrapa**, representa mais de 90% da produção nacional.
    
    
''')
with col2:
    st.image('https://images.unsplash.com/photo-1593535388526-a6b8556c5351?q=80&w=1169&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', caption='Foto de Tina Witherspoon no Unsplash')

st.write('---')