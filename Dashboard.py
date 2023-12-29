import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Home | TechChallenge FIAP :wine_glass:', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png', layout='wide')
aba1, aba2, aba3, aba4, aba5, aba6, aba7, aba8 = st.tabs(['Histórico', 'Produção', 'Exportação', 'Comercialização', 'Importação', 'Influências', 'Consumo', 'Conclusão'])
col1, col2 = st.columns(2)

with aba1:


    st.markdown('''
    ## O Vinho no Brasil
                    
    A história do vinho no Brasil se inicia junto com a história da colonização Portuguesa por aqui. A primeira videira foi plantada em 1532, na Capitania de São Vicente, por Brás Cubas, fundador da cidade de Santos. Contudo, essa primeira tentativa não deu certo porque o clima do litoral não era favorável para o cultivo da uva.
    
    Por isso, depois de alguns testes, na região do Tatuapé, em São Paulo, nasce a primeira vinha do Brasil. Algumas décadas depois, as missões jesuítas que rodavam o país inteiro chegaram na região Sul do país e, junto com eles, a cultura do vinho. Há registros de videiras cultivadas na região nos anos de 1626. Desde então, essa cultura se manteve, virou tradição e hoje, coloca o Brasil no mapa de um dos principais produtores e exportadores de vinhos do mundo.
    
    Hoje o Brasil tem forte presença no mercado internacional de vinhos tendo regiões produtivas não só no Rio Grande do Sul como também em Santa Catarina, Paraná, São Paulo, Minas Geraisl, Foiás, Bahia, Pernambuco e Ceará.
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
    ''')


st.markdown('[:arrow_up_small:[Topo da página]](#o-vinho-no-brasil)')

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