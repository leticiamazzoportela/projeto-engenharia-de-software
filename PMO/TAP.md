# Termo de Abertura do Projeto

## Implementação de uma Aplicação para Classificação de Macrófitas

### Controle de Versões
| Versão | Data | Autores | Notas da Revisão
|:--:|:--:|:--:|:--:|
| 0.0.1 | 21/08/2018 | Cláudia, Igor, Jonas, Letícia | Estrutura Inicial TAP |
| 0.0.2 | 24/08/2018 | Cláudia, Igor, Jonas, Letícia | Adicionados mais detalhes do projeto |
| 0.0.3 | 05/09/2018 | Cláudia, Igor, Jonas, Letícia | Adicionado requisitos do projeto |

## Sumário
1. [Objetivo do Documento](#od)
2. [Propósito](#prop)
3. [Descrição do Projeto](#desc)<!-- 4. [Objetivos do Projeto e Critérios de Sucesso](#obj) -->
4. [Requisitos do Projeto](#req)<!-- 6. [Escopo Preliminar](#escopo) --><!-- 7. [Principais Riscos do Projeto](#riscos) --><!-- 8. [Principais Entregas](#entregas) -->
5. [Cronograma de Marcos](#marcos)
6. [Partes Interessadas do Projeto](#pip)
7. [Requisitos para Aprovação do Projeto](#aprov)
8. [Gerente do Projeto](#ger)

<div id='od' />

## Objetivo do Documento
Autorizar o início do projeto, atribuir principais responsáveis e documentar requisitos iniciais, principais entregas, premissas e restrições.

<div id='prop' />

## Propósito
Com o intuito de atender às necessidades de um grupo de pesquisa da Universidade Estadual de Maringá (UEM), foi solicitada a implementação deste projeto, cujo objetivo é o de desenvolver uma aplicação para otimizar o processo de classificação de macrófitas.

<div id='desc' />
 
## Descrição do Projeto
O sistema em questão é aplicado à pesquisas em Ecologia de ambientes aquáticos continentais, as quais têm o objetivo de investigar padrões
biogeográficos de macrófitas aquáticas (plantas que vivem permanentemente ou
por alguns períodos do ano, com a parte fotossintetizante em contato com a água)
na América do Sul. Com base em dados ocorrência dessas plantas, pretendemos
identificar áreas de maior diversidade, famílias e táxons amplamente distribuídas,
famílias e táxons com áreas restritas de ocorrência, entre outros. Em adição, dados
de ocorrência das espécies serão correlacionados à variáveis ambientais para a
predição da área de distribuição geográfica das espécies no presente e no futuro,
considerando o efeito das mudanças climáticas. Para isso foram selecionados 40
artigos   científicos   que   forneceram   uma   lista   de   cerca   de   1900   espécies   de
macrófitas aquáticas com ocorrência na América do Sul. Desta forma, o produto
pretendido é um sistema capaz i) de validar os nomes das espécies de macrófitas
em   
online databases
,   trazendo   também   informações   acerca   da
taxonomia/ecologia/biologia   referentes   aos   nomes   aceitos,   ii)   de   congregar
informações de registros ocorrências dessas espécies de macrófitas no continente,
corrigindo   erros   e   indicando   padrões   e   tendências   considerando   as   bacias
hidrográficas Sul-Americanas. 

<!-- <div id='obj' />

## Objetivos do Projeto (SMART) e Critérios de Sucesso
A definir. -->

<div id='req' />

## Requisitos do Projeto
- O sistema deve validar o nome das espécies da lista de entrada (1900
espécies) com base nas informações disponibilizadas 
em online databases
 (Flora
do Brasil e PlantList), fornecendo o nome atualmente aceito e autor, bem como a
lista de sinonímias para cada nome válido ou aceito;

- Para   cada   espécie   válida   o   sistema   deve   buscar   e   extrair   das  
online
databases
 os seguintes informações: ordem, classe, família, tribo, forma de vida,
substrato, origem, endemismo e distribuição geográfica.

- O sistema deve buscar os dados de ocorrência de cada espécie (para o nome
aceito e suas sinonímias) nas plataformas Specieslink e GBIF;  

- O sistema deve executar um processo de triagem dos dados de ocorrências
disponibilizados pelo GBIF e Specieslink de modo a corrigir nomes duplicados,
erros de digitação, coordenadas ausentes, registros de grupos não plantas (ex.
peixes, insetos, répteis, etc), entre outras inconsistências.

- O sistema deverá fornecer gráficos/tabelas/mapas com as principais tendências dos dados   entre   as   14   grandes   bacias   Sul-Americanas   e   do
continente como um todo, como por exemplo, número de espécies de macrófitas
por bacia, família mais especiosa, família mais amplamente distribuída, etc. 

<!-- <div id='escopo' />

## Escopo Preliminar
A definir.

<div id='riscos' />

## Principais Riscos do Projeto
A definir.

<div id="entregas" /> 

## Principais Entregas
Detalhes a definir
-->

<div id="marcos" />

## Cronograma de Marcos
+ **Entrega 1:** 14/09/2018;
+ **Entrega 2:** 28/09/2018;
+ **Entrega 3:** 19/10/2018;
+ **Entrega 4:** 06/12/2018.

<div id="pip" />

## Partes Interessadas do Projeto
| Cliente | Instituição
|:--:|:--:|
| Tania | UEM |
| Karina | UEM |
| Dayani | UEM |

<div id="aprov" />

## Requisitos para Aprovação do Projeto

<div id="ger" />

## Gerentes do Projeto

- Igor Neves Faustino
- Cláudia L. P. Sampedro
- Letícia Mazzo Portela
- Jonas Felipe Alves