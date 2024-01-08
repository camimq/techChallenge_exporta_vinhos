import streamlit as st

st.set_page_config(page_title='Sobre o Projeto | TechChallenge FIAP', page_icon='https://cdn-icons-png.flaticon.com/512/763/763048.png')

st.image('img/header.jpg', caption='Imagem criada pelo Copilot do Edge')

with st.sidebar:     
    st.markdown(':sweat_smile: Feito por **Camila Queiroz - RM 351738**')

col20, col21 = st.columns(2)
with col20:
    with st.container(border=True):
        st.title('Sobre o Projeto')
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

st.markdown('---')
st.markdown('## Referências bibliográficas')
st.markdown('Abaixo, listo as fontes pesquisadas para a realização deste projeto:')
st.markdown('''
                - Vinho e Colonização conta a história da bebida durante  colonização portuguesa no Brasil
                
                    https://brasildevinhos.com.br/vinho-e-colonizacao-conta-a-historia-da-bebida-durante-colonizacao-portuguesa-no-brasil/

                - O Vinho no Brasil
                    
                    http://vinhobrasileiro.org/o-vinho-no-brasil/historia

                - G1: E o maior produtor mundial de vinho é...
                
                    https://g1.globo.com/pr/parana/especial-publicitario/porto-a-porto/guia-do-vinho-e-da-gastronomia/noticia/2023/10/03/e-o-maior-produtor-mundial-de-vinho-e.ghtml

                - Gazeta do Povo: Exportação de vinhos brasileiros avança 325% em cinco anos para os EUA e China
                
                    https://www.gazetadopovo.com.br/bomgourmet/negocios-e-franquias/exportacao-vinhos-brasileiros-avanca-eua-china/

                - Associação Brasileira de Enologia: Uma porta aberta para os vinhos brasileiros no Reino Unido
                
                    https://www.enologia.org.br/noticia/uma-porta-aberta-para-os-vinhos-brasileiros-no-reino-unido

                - G1: De olho na Copa, importadores britânicos miram no vinho brasileiro
                
                    https://g1.globo.com/brasil/noticia/2013/08/de-olho-na-copa-importadores-britanicos-miram-no-vinho-brasileiro.html

                - RBA: Crise no Paraguai é agravada pela situação econômica do país
                
                    https://www.redebrasilatual.com.br/mundo/crise-paraguai-situacao-economica/
                - Winepedia: O que é terroir e qual a sua importância?
                
                    https://www.wine.com.br/winepedia/curiosidades/o-que-e-terroir/?gad_source=1&gclid=CjwKCAiA1-6sBhAoEiwArqlGPqBVfEy3ShcVEa4p4DJVWdMs23FdzO9RkGySdv1qdvZIIxP3CZ_D0RoC9mcQAvD_BwE
                - Winepedia: Mudanças de clima impactam na produção de vinho? Entenda por quê
                
                    https://www.wine.com.br/winepedia/curiosidades/mudancas-de-clima-impactam-na-producao-de-vinho/
                - Canal Rural: Clima adverso reduz produção de vinhos e espumantes no Brasil
                
                    https://www.canalrural.com.br/agricultura/clima-adverso-reduz-producao-de-vinhos-e-espumantes-no-brasil/
            ''')
 
st.markdown('')
st.write('---')
st.write('### Quem fez :technologist:')
col3, col4 = st.columns(2)
with col3:
    st.write('**Autor:** Camila Queiroz - RM 351738')
    st.write('**Data de criação:** 26/12/2023')
    st.write('**Última atualização:** 26/12/2023')
    '''
     [![Title](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABDUlEQVR4AWP4////gOLB44D6nTcsGIo33QHi/zTGd0B2YTiAPpYjHIHNAf/piQk6wGPW8f/rLz8HYRCbXg5AWI4GQGJ0cwDY12gAJDbcHUA4CkZAIqQUK7Ts/m/SfxBMs5RupswBaACr+P47b/5zlG/5DyzZ/r/+8hNF7vuvP//nn3r0X6JhJ+0ccPrR+/+H7735jw9cf/n5v0D1Nuo5gBxQve06zR0AjoL7b7/+//zjN4bc+ScfaOeA33///k9Yfg4mDw7u/Xdeo6uhnQP6D93FMNxlxjF0ZbRzgMXEQ9iyI90cALIMJoccDXRzAK6CZog6YNQBow6gIx54Bwx4x2RAu2bAysoEZu9o7xgAQrvkxt3WZi0AAAAASUVORK5CYII=)](www.linkedin.com/in/camilaqueiroz) [![Repo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEX////4+Pi3ubtvcnZNUVU+Q0cpLjLr6+x3en0sMTYkKS59gIORk5aUl5n8/Pzw8PFTV1tbX2Pc3d5DSEzn5+g3PECLjpFKTlKFh4qxs7XCxMUwNTq/wcLh4uPV1tZzd3o/Q0jOz9CmqKpjZ2qfoaSrd37mAAABPUlEQVR4AW3TBZKEMBAF0B8GCHzcnbW5/xm30qEyknklcU/DgQpuYRTHUXgLFHw6SemkmcYrlcd8kRYlnlQ1PU0Fp434Qde75Qd+1FUQKiRZjyGfTGNjKhWMmSQXYO3Ibao3MlqBnSRzADhk/ycAdcqclSSHnEUD+KLt8KalMQMqpl3izU5jKxHQGCq8Ud80fq4VfuFZaIyQO4wVPEre5g+RrIAPJrkQSL8OPjv3htQmH8guU5uwgseeP7ITMYBnpdFgvlJPcx0zoLjjzS/FDrVRvH6xsqDYlLx29huRUaFx6YuI1mhKMbddf9trEzca7rmRk/FxpiRXiJO8FDBURyb4yfO7glC8TOpacmAc4ElMEWlc2oGckjwvYVFEB5wjouE6uLBwquypQym/scKrM4njElYaJy182q15aDj/oQMZkS8JH3IAAAAASUVORK5CYII=)](https://github.com/camimq/camimq)
    '''
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('[:arrow_up_small:[Topo da página]](https://techchallengeexportavinhosfiap.streamlit.app/Sobre_o_projeto#sobre-o-projeto)')