import streamlit as st

st.set_page_config(page_title='O Projeto | TechChallenge FIAP :wine_glass:', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png')

st.image('https://www.freewebheaders.com/wp-content/gallery/drinks/awesome-wine-barrel-and-bottle-with-red-wine-glasses-web-header.jpg', caption='Foto retirada de Free Webheaders.com')

st.title('O Projeto')
st.markdown('''
O objetivo do projeto, é entregar a análise de um conjunto de dados disponível no [site da Embrapa](https://www.cnpuv.embrapa.br/vitibrazil/index.php?opcao=opt_02) e que contém informações sobre a quantidade de uvas processadas, produção e comercialização de vinhos, sucos e derivados, proveninentes do Estado do Rio Grande do Sul e que, ainda de acordo com a **Embrapa**, representa mais de 90% da produção nacional.
    
Este projeto é parte integrante da finalização do primeiro módulo do curso de Pós-Graduação em Data Analytics da FIAP.
    
## Tarefa

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
    
''')

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