import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# configura propriedades da página: título, ícone, layout etc
st.set_page_config(page_title='Home | TechChallenge FIAP', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png', layout='wide', initial_sidebar_state="expanded", menu_items={ 'About': '# Fale comigo! :smile: \n Para ver mais sobre o projeto, acesse: [GitHub](https://github.com/camimq/techChallenge_exporta_vinhos). Este é um projeto acadêmico de pós-gradução do curso de Data Analytics da PosTech FIAP.'})

# Formata números da aplicação
def formata_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'

aba1, aba2, aba3 = st.tabs(['Histórico', 'Análise', 'Conclusão'])

# **** [[INÍCIO]] ABA 1 - HISTÓRICO **** #
with aba1:

    with st.sidebar:     
        st.markdown(':sweat_smile: Feito por **Camila Queiroz - RM 351738**')

    st.image('img\_a2fbca62-86ef-42be-95de-3e1025f90104.jpg', caption='Imagem gerada pelo Copilot do Edge', use_column_width=True)
    col20, col21 = st.columns(2)
 
    with col20: 
        st.markdown('''
            # O Vinho no Brasil
                            
            A história do vinho no Brasil se inicia junto com a história da colonização Portuguesa por aqui. A primeira videira foi plantada em 1532, na Capitania de São Vicente, por Brás Cubas, fundador da cidade de Santos. Contudo, essa primeira tentativa não deu certo porque o clima do litoral não era favorável para o cultivo da uva.
            
            Por isso, depois de alguns testes, na região do Tatuapé, em São Paulo, nasce a primeira vinha do Brasil. Algumas décadas depois, as missões jesuítas que rodavam o país inteiro chegaram na região Sul do país e, junto com eles, a cultura do vinho. Há registros de videiras cultivadas na região nos anos de 1626. Desde então, essa cultura se manteve, virou tradição e hoje, coloca o Brasil no mapa de um dos principais produtores e exportadores de vinhos do mundo.
            
            Hoje o Brasil tem forte presença no mercado internacional de vinhos tendo regiões produtivas não só no Rio Grande do Sul como também em Santa Catarina, Paraná, São Paulo, Minas Gerais, Foiás, Bahia, Pernambuco e Ceará.
        ''')
    with col21:
        st.markdown('')
        st.markdown('''
        ### O Brasil no mapa global da produção de vinhos
                
        Nos anos 90, com a abertura da economia brasileira, o país passou a importar insumos e equipamentos que possibilitaram modernizar o processo de produção de vinhos, proporcionando um salto considerável na qualidade dos produtos nacionais. Além disso, para os consumidores, também houve crescimento na oferta de rótulos, trazendo concorrência e, junto com ela, uma comunidade cada vez mais exigente e interessada em vinhos.
        
        Com essa comunidade crescente de consumidores e amantes do vinho, veio junto o desenvolvimento técnico de profissionais do segmento, que ajudou a trazer o nível e exigência que os consumidores buscavam. Com isso, em 1995, através da iniciativa dos produtores de vinho brasilieiros, o Brasil aderiu à Organização Internacional da Uva e do Vinho. A partir daí, o país passou a ter acesso a dados e informações sobre o mercado mundial de vinhos e participar de discussões e decisões sobre o setor.
        
        Essa nova realidade, traz visibilidade para o Brasil e, consequentemente, para os vinhos produzidos aqui. Com isso, o país passa a ser reconhecido como um dos principais produtores de vinho do mundo.
    ''')
    st.markdown('''
        ## O mercado do vinho hoje

        Segundo o site [Vinho brasileiro](https://vinhobrasileiro.org/o-vinho-no-brasil/historia), o Brasil hoje, tem consumo per capita/ano de 2,7 litros de vinho ao ano. Esse número se deve ao fato de que o acesso ao vinho hoje é muito mais facilitado. Isso se deve ao fato de que a capilaridade de distribuidores e pontos de venda presenciais, além do incremento de vendas on-line.

        O Brasil hoje conta com 1100 vinícolas. Delas, 50 mil famílias vivem da produção de uvas e vinhos e são os responsáveis diretos por tornar o Brasil o 15º maior produtor de vinhos do mundo. De acordo com a [última medição](https://g1.globo.com/pr/parana/especial-publicitario/porto-a-porto/guia-do-vinho-e-da-gastronomia/noticia/2023/10/03/e-o-maior-produtor-mundial-de-vinho-e.ghtml), o Brasil produziu 3,2 milhões de litros de vinho, um crescimento de 1,2% em relação a medição anterior.

        De acordo com os dados de 2022, a produção nacional aumentou 14% em relação às últimas cinco safras. Após oito anos de encolhimento, o setor voltou a crescer e hoje, produtores de vinho e toda a cadeia produtiva do setor, estão otimistas com o que o futuro reserva.
                    
        [:arrow_up_small:[Topo da página]](#o-vinho-no-brasil)
    ''')
# **** [[FIM]] ABA 1 - HISTÓRICO **** #
 
# **** [[INÍCIO]] ABA 2 - ANÁLISE **** #    
with aba2:
    st.markdown('# Resumo das Exportações')
    st.markdown('''A tabela abaixo representa o resumo das exportações dos vinhos de 2008 à 2022, ordenado por valor total em USD. Através dessa tabela, é possível notar que o Paraguai é o principal comprador de vinhos do Brasil, seguido de Russia, Estados Unidos, China e Reino Unido, considerando valores de Receita como critério de ordenação.
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
    # soma_valores = df_exportacao_consolidado_reordenado['Valor Total (US$)'].sum()
    soma_valores = formata_numero(df_exportacao_consolidado['Qtd. Total (L)'].sum(), '')

    # soma total de litros exportados
    soma_litros = formata_numero(df_exportacao_consolidado['Qtd. Total (L)'].sum(), '')

    st.dataframe(df_exportacao_consolidado_reordenado, use_container_width=True)
    st.markdown('Entre 2008 e 2022, o Brasil exportou um **total de ' f'$ {soma_valores}' ' dólares em vinhos, que corresponde a 'f'{soma_litros}' ' litros produzidos e exportados**.')

    st.markdown('---')
    
    st.markdown('# Top 5 Importadores')
    st.markdown('Se olharmos para os 5 principais exportadores de vinho do Brasil, notaremos que estes são responsáveis por 50% do total de exportações do país.')
    
    col3, col4 = st.columns(2)
    with col3:
        st.metric('Receita Total | Top 5 Importadores', formata_numero(df_exportacao_consolidado['Valor Total (US$)'].head().sum(), 'US$'))
    
    with col4:
        st.metric('Total de Vinnho Exportado (L) | Top 5 Importadores', formata_numero(df_exportacao_consolidado['Qtd. Total (L)'].head().sum(), ''))

    # constrói DataFrame do Gráfico de Barras Top 5
    dados_grafico_barras = df_exportacao_consolidado.head()
    dados_grafico_barras = dados_grafico_barras.set_index('País de destino')
    dados_grafico_barras=dados_grafico_barras.drop(columns=('País de Origem'))

    fig_top5_exportadores = px.bar(dados_grafico_barras, x=dados_grafico_barras.index,
                                   y=dados_grafico_barras.columns, 
                                   barmode='group',
                                   title = 'Top 5 Importadores | Receita (US$) e Quantidade (L) Exportados',
                                )
    fig_top5_exportadores.update_xaxes(title_text="Ano")
    fig_top5_exportadores.update_yaxes(title_text="Valor")
    
    st.markdown('Por isso, de início, temos duas constatações importantes:')
    col5, col6 = st.columns(2)


    with col5:
        st.markdown('''                     
            **1.** O Brasil tem como primeiro objetivo, manter relacionamento aproximado com Paraguai, Rússia, Estados Unidos, China e Reino Unido, **com o objetivo de, inicialmente, manter o volume de exportações** e, posteriormente, entender ações cabíveis e estudar espaço para crescimento, se houver.
        ''')
    with col6:
         st.markdown('''
            **2.** Entender como a outra porção de mercado pode ser explorada para que a penetração do Brasil nestes mercados seja maior, levando o país a um crescimento no _market share_ destes países e elevando a nossa posição no _ranking_ de exportadores de vinho.  
        ''')
    
    st.plotly_chart(fig_top5_exportadores, use_container_width=True)

    st.markdown('''
    Entre os **top 5 importadores**, nota-se uma imediata oportunidade de crescimento entre Estados Unidos, China e Reino Unido.
    
    Segundo a [Ideal Consulting](https://www.gazetadopovo.com.br/bomgourmet/negocios-e-franquias/exportacao-vinhos-brasileiros-avanca-eua-china/), o interesse nos espumantes produzidos no Brasil teve um crscimento relevante nos últimos anos, especialmente entre Estados Unidos e China. Segundo esta mesma consultoria, o Brasil é o 4º maior produtor deste tipo de vinho no pais. **Portanto, esta é uma janela que possibilita o crescimento do Brasil nesses dois mercados.**
    
    Para a [Associação Brasileira de Enologia](https://www.enologia.org.br/noticia/uma-porta-aberta-para-os-vinhos-brasileiros-no-reino-unido), a principal porta de entrada para o mercado britânico, segue sendo o International Wine Challenge IIWC), que é o maior concurso de vinhos do mundo e que, desde 2018, tem premiado vinhos brasileiros. Se para este mercado, esse tipo de premiação valida a qualidade e chancela a entrada dos produtos nacionais neste mercado, **é importante que o Brasil siga fortalecendo sua presença não só neste concurdo como também em todos os eventos que circulem este, para que ganhemos visibilidade e espaço**.
    ''')

    st.markdown('---')
    
    st.markdown('# Evolução das Exportações')
    
    # constroi DataFrames e gráficos que serão utilizados #

    ## cria DataFrame exportacao_por_pais
    
    ### cria df_exportacao, utilizando a base de dados original
    df_exportacao = pd.read_csv('https://raw.githubusercontent.com/camimq/techChallenge_exporta_vinhos/main/bases/ExpVinho.csv', sep=';')

    ### cria df_exportacao_por_pais - LITROS
    exportacao_por_pais = df_exportacao[['País', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']]

    #### cria coluna de soma total para quantidade de exportação
    exportacao_por_pais['Qtd. Total (L)'] = exportacao_por_pais ['2008']+exportacao_por_pais ['2009']\
    +exportacao_por_pais ['2010']+exportacao_por_pais ['2011']+exportacao_por_pais ['2012']\
    +exportacao_por_pais ['2013']+exportacao_por_pais ['2014']+exportacao_por_pais ['2015']\
    +exportacao_por_pais ['2016']+exportacao_por_pais ['2017']+exportacao_por_pais ['2018']\
    +exportacao_por_pais ['2019']+exportacao_por_pais ['2020']+exportacao_por_pais ['2021']\
    +exportacao_por_pais ['2022']

    #### exclui linhas de total com valor == 0
    exportacao_por_pais.drop(exportacao_por_pais.loc[exportacao_por_pais['Qtd. Total (L)']==0].index, inplace=True)

    #### ordenando valor da maior quantidade para a menor
    exportacao_por_pais = exportacao_por_pais.sort_values(by='Qtd. Total (L)', ascending=False)

    ### cria valor_exportacao_por_pais - RECEITA
    valor_exportacao_por_pais = df_exportacao[['País', '2008.1', '2009.1', '2010.1', '2011.1', '2012.1', '2013.1', '2014.1', '2015.1', '2016.1', '2017.1', '2018.1', '2019.1', '2020.1', '2021.1', '2022.1']]

    #### cria coluna de soma total para receita de exportação
    valor_exportacao_por_pais['Valor Total (US$)'] = valor_exportacao_por_pais ['2008.1']+valor_exportacao_por_pais ['2009.1']\
    +valor_exportacao_por_pais ['2010.1']+valor_exportacao_por_pais ['2011.1']  +valor_exportacao_por_pais ['2012.1']\
    +valor_exportacao_por_pais ['2013.1']+valor_exportacao_por_pais ['2014.1']  +valor_exportacao_por_pais ['2015.1']\
    +valor_exportacao_por_pais ['2016.1']+valor_exportacao_por_pais ['2017.1']  +valor_exportacao_por_pais ['2018.1']\
    +valor_exportacao_por_pais ['2019.1']+valor_exportacao_por_pais ['2020.1']  +valor_exportacao_por_pais ['2021.1']\
    +valor_exportacao_por_pais ['2022.1']

    #### exclui linhas com valor monetário total == 0
    valor_exportacao_por_pais.drop(valor_exportacao_por_pais.loc[valor_exportacao_por_pais['Valor Total (US$)']==0].index, inplace=True)

    #### ordenando valor do maior valor para o menor
    valor_exportacao_por_pais = valor_exportacao_por_pais.sort_values(by='Valor Total (US$)', ascending=False)

    ## cria DataFrame para desenvolvimento de gráfico de linha - LITROS
    dados_grafico_linha_qtd = exportacao_por_pais.set_index('País')
    dados_grafico_linha_qtd = dados_grafico_linha_qtd.drop('Qtd. Total (L)', axis=1)

    ### transpondo tabela
    dado_qtd=dados_grafico_linha_qtd.head()
    dado_qtd = dado_qtd.T
    
    # cria dataframe desenvolvimento do gráfico de linha - RECEITA
    dados_grafico_linha_valor = valor_exportacao_por_pais.set_index('País')
    dados_grafico_linha_valor = dados_grafico_linha_valor.drop('Valor Total (US$)', axis=1)
    
    ## atualiza os nomes de colunas
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

    # transpondo tabela
    dado_valor = dados_grafico_linha_valor.head()
    dado_valor = dado_valor.T
    
    ## evolução de quantidade para o top 5 compradores - LITROS
    fig_evolucao_volume_top_five = px.line(dado_qtd,
                x=dado_qtd.index,
                y=dado_qtd.columns, 
                markers=True,
                title='Evolução de exportação para os 5 maiores compradores (em L)',
                width=700
            )
    fig_evolucao_volume_top_five.update_xaxes(title_text="Ano")
    fig_evolucao_volume_top_five.update_yaxes(title_text="Volume")
    
    ## evolução de receita para o top 5 compradores
    fig_evolucao_receita_top_five = px.line(dado_valor,
                x=dado_valor.index, 
                y= dado_valor.columns, 
                markers=True, 
                template='plotly_white', 
                title='Evolução de exportação para os 5 maiores compradores (em US$)', 
                width=700
            )
    fig_evolucao_receita_top_five.update_xaxes(title_text="Ano")
    fig_evolucao_receita_top_five.update_yaxes(title_text="Valor")  

    # cria gráfio de evolução de exportação Espanha
    fig_qtd_evolucao_ES = px.line(dado_qtd,
                x=dado_qtd.index,
                y='Espanha',
                markers=True,
                template='plotly_white',
                title='Evolução de exportação para os Espanha (L)',
                width=700
            )
    
    
    dado_qtd_UK=dados_grafico_linha_qtd.head(10)
    dado_qtd_UK= dado_qtd_UK.T
    
    # cria gráfio de evolução de exportação Reino Unido
    fig_qtd_evolucao_UK = px.line(dado_qtd_UK,
        x=dado_qtd_UK.index,
        y='Reino Unido',
        markers=True,
        template='plotly_white',
        title='Evolução de exportação para os Reino Unido (L)',
        width=700
    )

    # cria dataframe com valores de quantidade e valor por país
    dados_valores_totais_pais = df_exportacao_consolidado.drop(columns=('País de Origem'))

    ##  cria df com quantidade exportada total por ano
    dados_qtd_total_anual = dados_grafico_linha_qtd.sum()
    dados_qtd_total_anual = pd.DataFrame(dados_qtd_total_anual)

    dados1_qtd_total_anual = dados_qtd_total_anual.reset_index()
    dados1_qtd_total_anual.index.rename('novoIndex', inplace=True)

    ##  cria df com valor exportada total por ano
    dados_valor_total_anual = dados_grafico_linha_valor.sum()
    dados_valor_total_anual = pd.DataFrame(dados_valor_total_anual)

    dados2_valor_total_anual = dados_valor_total_anual.reset_index()
    dados2_valor_total_anual.index.rename('novoIndex', inplace=True)

    ## cria dataframe com valores totais de exportação por ano(quantidade e valores)
    dados_totais_qtd_valor = pd.merge(dados1_qtd_total_anual, dados2_valor_total_anual, on='novoIndex', how='left')
    dados_totais_qtd_valor = dados_totais_qtd_valor.drop('index_y', axis=1)

    ## organizando novo DataFrame para plotar os gráficos
    dados_totais_qtd_valor.rename(columns={'index_x' : 'Ano', '0_x' : 'Quantidade', '0_y' : 'Valor'}, inplace=True)
    dados_totais_qtd_valor = dados_totais_qtd_valor
    dados_totais_qtd_valor = dados_totais_qtd_valor.set_index('Ano')

    ### evolução da quantidade e valor de exportação no período de 2008 à 2022
    fig_qtd_versus_valor = px.line(dados_totais_qtd_valor,
                x=dados_totais_qtd_valor.index,
                y=dados_totais_qtd_valor.columns,
                markers=True,
                title='Evolução | Quantidade x Valor',
    )
    fig_qtd_versus_valor.update_xaxes(title_text="Ano")
    fig_qtd_versus_valor.update_yaxes(title_text="Valor") 

    # --------------------------------------------------------------------------------------#

    with st.expander('##### :heavy_exclamation_mark: Disclaimer:\n **Fato importante Sobre Espanha e Reino Unido**'):
        st.markdown('''
            Abaixo, apresentaremos um conjunto de gráficos que representam a evolução das exportações em termos de volume e receita, para os 5 maiores compradores de vinho do Brasil, entre 2008 e 2022. Desde o início desta análise, consideramos **receita** como critério para definição de ranqueamento dos países que aparecem na análise. Desta forma, tratamos sempre Paraguai, Rússia, Estados Unidos e Reino Unido como principais parceiros do Brasil na compra de vinhos; os **Top 5 Importadores**.
            
            Contudo, como verá nos gráficos de evolução onde os 5 principais consumidores são alinhados para comparar a evolução no **volume** de compras e no montante de **receitas**, há um comportamento inesperado quando olhamos para volume: Espanha aparece em 5º lugar, ao invés do Reino Unido.
        ''')

        col7, col8 = st.columns(2)
        with col7:
            st.plotly_chart(fig_qtd_evolucao_ES, use_container_width=True)
        with col8:
            st.plotly_chart(fig_qtd_evolucao_UK, use_container_width=True)

        st.markdown('''
            Nos gráficos acima, mostramos a evolução da volumetria de cada país (Espanha e Reino Unido). É possível notar que, pontualmente, em 2013, a Espanha aparece com volume superior ao do Reino Unido que, neste mesmo ano, tem uma queda relevante em seu volume, em relação ao mesmo período do ano anterior.
            
            Em contrapartida, olhando para o mesmo gráfico, notamos que o Reino Unido, em 2014, tem um salto na importação de vinhos nacionais. Isso se deve a uma aposta feita pelo país, através da Copestick Murray (uma das principais importadoras britânicas) que enxergou na Copa do Mundo (2014) e nas Olimpíadas (2016), ambas realizadas no Brasil, uma oportunidade de crescimento visto que o país atraiu a atenção do mundo neste período de 3 anos em que os maiores eventos esportivos do mundo aconteceram por aqui. Sendo assim, a [Copestick Murray, junto com a Vinícola Aurora, produziram dois vinhos com um _blend_ pensado especialmente para o mercado britânico](https://g1.globo.com/brasil/noticia/2013/08/de-olho-na-copa-importadores-britanicos-miram-no-vinho-brasileiro.html). Através desse _deal_, as expectativas eram de que o Brasil exportasse para o Reuno Unido o total de 94,l mil litros de vinho em 2013. E deu certo! Se olharmos os resultados de venda 2013 / 2014, temos um total muito superior ao estimado inicialmente.
        ''')
    st.markdown('## Sobre a evolução das exportações')
    st.write('''
        Nos últimos 15 anos, o Brasil evoluiu de forma nítida em relação a valores e volumes exportados. Estamos falando de crescimento constante e consistente, que nos coloca em uma posição de destaque no mercado mundial de vinhos.
    ''')
    col9, col10 = st.columns(2)
    with col9:
        st.plotly_chart(fig_evolucao_volume_top_five, use_container_width=True)
        st.markdown('''
            A Russia traz em 4 anos (2008, 2009, 2012 e 2013) o consumo de volumes expressivos concentrados somente nesse período. Se considerarmos a série histórica de 15 anos analisados, é possível dizer que, durante todo este período, a Russia tem 44% do total de vinho exportado, sem nenhuma razão aparente ou sem nenhum tipo de correlação. 
        ''')
    with col10:    
        st.image('img\evolucao_sem_russia.png', caption='Imagem do gráfico de evolução sem a Rússia')
        st.markdown('''
            Mesmo em segundo lugar, o Paraguai tem evolução constante, especialmente, à partir de 2017 e se mantém até 2019, quando há uma queda no consumo, [devido a uma crise política agravada pela situação econômica do país](https://www.redebrasilatual.com.br/mundo/crise-paraguai-situacao-economica/).
         ''')
    st.markdown('---')
    col11, col12 = st.columns(2)
    with col11:
        st.plotly_chart(fig_qtd_versus_valor, use_container_width=True)
    with col12:
        st.markdown('''
            Uma das razões que pode explicar o crescimento constante do valor em relação à quantidade (especialmente à partir de 2010), está no aumento do dólar. Se olharmos para a evolução do dólar no período de 2008 à 2022, veremos que, em 2008, o dólar estava cotado a R$ 1,60. Em 2022, a cotação do dólar está em R$ 6,00. Isso significa que, em 2022, o dólar está 3,75 vezes mais caro do que em 2008 e, todo o contexto de negociações de exportação de vinho, está contido nesse valor.
                    
            Além disso, influências políticas também devem ser consideradas. Na América do Sul, organizações como BRICS e Mercosul, tem papel definitivo na relação comercial entre os países participantes, influenciando positivamente e de forma direta os resultados alcançados afim de fortalecer a economia da região e trazer maior visibilidade para o mercado internacional (com destaque para os países fora do eixo LATAM).
        ''')
        st.markdown('### Influências na produção do vinho que impactam diretamente na exportação')
    st.markdown('[:arrow_up_small:[Topo da página]](#e0c02a73)')
# **** [[FIM]] ABA 2 - ANÁLISE **** #    
        
# **** [[INÍCIO]] ABA 3 - PLANO DE AÇÃO / PRÓXIMOS PASSOS **** #   
   
with aba3:
    st.markdown('# Plano de Ação / Próximos Passos')
    col22, col23 = st.columns(2)
    with col22:
        st.markdown('''
            À partir das análises feitas até aqui, é possível definir algumas ações que podem ser tomadas para que o Brasil siga crescendo no mercado internacional de vinhos.
            
            Os pontos abordados nos tópicos ao lado, servem como base para entender o nível de investimento e dimensionar parte do trabalho neste primeiro momento. O trabalho de desenvolver e consolidar um país no mercado internacional, nunca é feito de forma rápida ou com trabalho mensurável finito. Mas, uma vez que temos a dimensão do que existe e o espaço que é possível ocupar, entendendo o tamanho e a importância que este mercado pode terno papel de crescimento da economia brasileira, torna-se viável considerar as ações e o investimento para que este mercado continue crescendo e se profissionalizando.
            
            Desta forma, consideramos que investir em vinículas ou em produtores independentes no médio prazo, trará retornos relevantes para o país e, também, para os envolvidos neste mercado, sejam produtores, investidores e toda a cadeia produtiva direta e indireta.    
        ''')

    with col23:
        st.markdown('#### :dart: Ações / Próximos Passos')
        col24, col25 = st.columns(2)
        with col24:    
            with st.container(border=True):
                st.markdown('''
                - Entre os TOP 5 Importadores, definir como prioridade para Estados Unidos e China, o aumento de venda de vinhos espumantes, visto que este é o principal interesse destes países em relação aos produtos que oferecemos.
                - Para o Reino Unido, seguir investindo em ações que fortaleçam a presença do Brasil no International Wine Challenge (IWC), que é o maior concurso de vinhos do mundo e que, desde 2018, tem premiado vinhos brasileiros. Se para este mercado, esse tipo de premiação valida a qualidade e chancela a entrada dos produtos nacionais neste mercado, é importante que o Brasil siga fortalecendo sua presença não só neste concurdo como também em todos os eventos que circulem este, para que ganhemos visibilidade e espaço.
            ''')
        with col25:
            with st.container(border=True):
                st.markdown('''
                    - Entre os TOP 5 Importadores, definir como prioridade para Estados Unidos e China, o aumento de venda de vinhos espumantes, visto que este é o principal interesse destes países em relação aos produtos que oferecemos.
                    - Para o Reino Unido, seguir investindo em ações que fortaleçam a presença do Brasil no International Wine Challenge (IWC), que é o maior concurso de vinhos do mundo e que, desde 2018, tem premiado vinhos brasileiros. Se para este mercado, esse tipo de premiação valida a qualidade e chancela a entrada dos produtos nacionais neste mercado, é importante que o Brasil siga fortalecendo sua presença não só neste concurdo como também em todos os eventos que circulem este, para que ganhemos visibilidade e espaço.
                ''') 
# **** [[INÍCIO]] ABA 3 - PLANO DE AÇÃO / PRÓXIMOS PASSOS **** #  