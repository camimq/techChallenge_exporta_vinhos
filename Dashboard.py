import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Home | TechChallenge FIAP :wine_glass:', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png')

# Formata números da aplicação
def formata_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'

aba1, aba2, aba3 = st.tabs(['Histórico', 'Análise', 'Conclusão'])
col1, col2 = st.columns(2)

with aba1:

    st.markdown('''
    # O Vinho no Brasil
                    
    A história do vinho no Brasil se inicia junto com a história da colonização Portuguesa por aqui. A primeira videira foi plantada em 1532, na Capitania de São Vicente, por Brás Cubas, fundador da cidade de Santos. Contudo, essa primeira tentativa não deu certo porque o clima do litoral não era favorável para o cultivo da uva.
    
    Por isso, depois de alguns testes, na região do Tatuapé, em São Paulo, nasce a primeira vinha do Brasil. Algumas décadas depois, as missões jesuítas que rodavam o país inteiro chegaram na região Sul do país e, junto com eles, a cultura do vinho. Há registros de videiras cultivadas na região nos anos de 1626. Desde então, essa cultura se manteve, virou tradição e hoje, coloca o Brasil no mapa de um dos principais produtores e exportadores de vinhos do mundo.
    
    Hoje o Brasil tem forte presença no mercado internacional de vinhos tendo regiões produtivas não só no Rio Grande do Sul como também em Santa Catarina, Paraná, São Paulo, Minas Gerais, Foiás, Bahia, Pernambuco e Ceará.
    ''')

    st.image('https://brasildevinhos.com.br/wp-content/uploads/2023/11/Imagem-2.jpeg', caption='Imagem retirada do site Brasil de Vinhos')
    
    st.markdown('''
    ### O Brasil no mapa global da produção de vinhos
            
    Nos anos 90, com a abertura da economia brasileira, o passou a importar insumos e equipamentos que possibilitaram modernizar o processo de produção de vinhos, proporcionando um salto considerável na qualidade dos produtos nacionais. Além disso, para os consumidores, também houve crescimento na oferta de rótulos, trazendo concorrência e, junto com ela, uma comunidade cada vez mais exigente e interessada em vinhos.
    Com essa comunidade crescente de consumidores e amantes do vinho, veio junto o desenvolvimento técnico de profissionais do segmento, que ajudou a trazer o nível e exigência que os consumidores buscavam. Com isso, em 1995, através da iniciativa dos produtores de vinho brasilieiros, o Brasil aderiu à Organização Internacional da Uva e do Vinho. A partir daí, o país passou a ter acesso a dados e informações sobre o mercado mundial de vinhos e participar de discussões e decisões sobre o setor.

    ## O mercado do vinho no Brasil hoje

    Segundo o site [Vinho brasileiro](https://vinhobrasileiro.org/o-vinho-no-brasil/historia), o Brasil hoje, tem consumo per capita/ano de 2,7 litros de vinho ao ano. Esse número se deve ao fato de que o acesso ao vinho hoje é muito mais facilitado. Isso se deve ao fato de que a capilaridade de distribuidores e pontos de venda presenciais, além do incremento de vendas on-line.

    O Brasil hoje conta com 1100 vinícolas. Delas, 50 mil famílias vivem da produção de uvas e vinhos e são os responsáveis diretos por tornar o Brasil o 15º maior produtor de vinhos do mundo. De acordo com a [última medição](https://g1.globo.com/pr/parana/especial-publicitario/porto-a-porto/guia-do-vinho-e-da-gastronomia/noticia/2023/10/03/e-o-maior-produtor-mundial-de-vinho-e.ghtml), o Brasil produziu 3,2 milhões de litros de vinho, um crescimento de 1,2% em relação a medição anterior.

    De acordo com os dados de 2022, a produção nacional aumentou 14% em relação às últimas cinco safras. Após oito anos de encolhimento, o setor voltou a crescer e hoje, produtores de vinho e toda a cadeia produtiva do setor, estão otimistas com o que o futuro reserva.
                
    [:arrow_up_small:[Topo da página]](#o-vinho-no-brasil)
    ''')

with aba2:
    st.markdown('# Tabela de Análise')
    st.markdown('''## Resumo das Exportações
A tabela abaixo representa o resumo das exportações dos vinhos de 2008 à 2022, ordenado por valor total em USD. Através dessa tabela, é possível notar que o Paraguai é o principal comprador de vinhos do Brasil, seguido de Russia, Estados Unidos, China e Reino Unido.
''')
    df_exportacao_consolidado = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/dfExportacaoConsolidado.csv')
    
    # insere widget de soma de valores de exportação (receita + litros)
    col1, col2 = st.columns(2)
    with col1:
            st.metric('Receita Total em  US$', formata_numero(df_exportacao_consolidado['Valor Total (US$)'].sum(), 'US$'))

    with col2:
         st.metric('Total de Vinho Exportado (L)', formata_numero(df_exportacao_consolidado['Qtd. Total (L)'].sum(), ''))
    
    # tras coluna país para o começo da tabela
    df_exportacao_consolidado_reordenado = df_exportacao_consolidado.sort_index(axis=1)

    # adiciona o país de origem
    df_exportacao_conssolidado_reordenado = df_exportacao_consolidado_reordenado['País de Origem'] = 'Brasil'

    # soma total de exportações
    soma_valores = df_exportacao_consolidado_reordenado['Valor Total (US$)'].sum()

     # soma total de litros exportados
    soma_litros = df_exportacao_consolidado['Qtd. Total (L)'].sum()

    st.dataframe(df_exportacao_consolidado_reordenado, use_container_width=True)
    st.markdown('Entre 2008 e 2022, o Brasil exportou um total de ' f'**$ {soma_valores}' ' dólares** em vinhos, totalizando ' f'**{soma_litros}' ' milhões de litros**.')
    
    st.markdown('Se olharmos para os 5 principais exportadores de vinho do Brasil, notaremos que estes, são responsáveis por 50% do total de exportações do país. Por isso, é possível olhar para este quadro de duas formas:')
    
    st.markdown(''' 
        **1.** O Brasil tem como primeiro objetivo, manter relacionamento aproximado com Paraguai, Rússia, Estados Unidos, China e Reino Unido, **com o objetivo de, inicialmente, manter o volume de exportações** e, posteriormente, entender ações cabíveis e estudar espaço para crescimento, se houver.

        **2.** Entender como a outra porção de mercado pode ser explorada para que a penetração do Brasil nestes mercados seja maior, levando o país a um crescimento no _market share_ destes países e elevando a nossa posição no _ranking_ de exportadores de vinho.  
    ''')
