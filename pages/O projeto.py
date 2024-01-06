import streamlit as st

st.set_page_config(page_title='O Projeto | TechChallenge FIAP :wine_glass:', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png')

st.image('https://www.freewebheaders.com/wp-content/gallery/drinks/awesome-wine-barrel-and-bottle-with-red-wine-glasses-web-header.jpg', caption='Foto retirada de Free Webheaders.com')

col20, col21 = st.columns(2)
with col20:
    with st.container(border=True):
        st.title('O Projeto')
        st.markdown('''
            Este projeto é parte integrante da finalização do primeiro módulo do curso de Pós-Graduação em Data Analytics da FIAP.
            
            Foi desenvolvido por ***Camila Queiroz - RM351738***, aluna do curso de Pós-Gradução em Data Analytics da Pós-Tech FIAP / Alura.
            
            Neste projeto, estão sendo utilizadas técnicas e conceitos apresentados no primeiro módulo do curso, para o desenvolvimento de uma análise exploratória, que trará como resultado um plano de ação para investidores que desejam se envolver no mercado de exportação de vinhos e derivados, auxiliando o Brasil a se consolidar como um dos principais países exportadores do mundo.
        ''')
with col21:
    with st.container(border=True):
        st.title('Objetivo')
        st.markdown('''
            O objetivo do projeto é analisar um conjunto de dados disponível no site da [Embrapa](https://www.cnpuv.embrapa.br/vitibrazil/index.php?opcao=opt_02), que contém informações sobre a produção e comercialização de uvas, vinhos, sucos e derivados no Estado do Rio Grande do Sul. Essa região, segundo a **Embrapa**, representa mais de 90% da produção nacional.
            
            O montante de exportação dos ***últimos 15 anos (2008 à 2022)** será avaliado, através das técnicas e conceitos apresentados durante o primeiro módulo do curso, de forma que, ao fim desta análise, tenhamos um panorama geral e um plano de ação para que o Brasil siga se consolidando como um dos principais atores no mercado de exportação de vinhos e derivados.
        ''')  
st.markdown('')
st.write('---')
st.write('#### Quem fez :technologist:')
col3, col4 = st.columns(2)
with col3:
    st.write('**Autor:** Camila Queiroz - RM 351738')
    st.write('**Data de criação:** 26/12/2023')
    st.write('**Última atualização:** 26/12/2023')

    '''
     [![Title](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABDUlEQVR4AWP4////gOLB44D6nTcsGIo33QHi/zTGd0B2YTiAPpYjHIHNAf/piQk6wGPW8f/rLz8HYRCbXg5AWI4GQGJ0cwDY12gAJDbcHUA4CkZAIqQUK7Ts/m/SfxBMs5RupswBaACr+P47b/5zlG/5DyzZ/r/+8hNF7vuvP//nn3r0X6JhJ+0ccPrR+/+H7735jw9cf/n5v0D1Nuo5gBxQve06zR0AjoL7b7/+//zjN4bc+ScfaOeA33///k9Yfg4mDw7u/Xdeo6uhnQP6D93FMNxlxjF0ZbRzgMXEQ9iyI90cALIMJoccDXRzAK6CZog6YNQBow6gIx54Bwx4x2RAu2bAysoEZu9o7xgAQrvkxt3WZi0AAAAASUVORK5CYII=)](www.linkedin.com/in/camilaqueiroz) [![Repo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/camimq/camimq)
    '''
    st.markdown("<br>", unsafe_allow_html=True)