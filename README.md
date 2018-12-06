# Implementação de uma Aplicação para Classificação de Macrófitas

[![Build Status](https://travis-ci.org/leticiamazzoportela/projeto-engenharia-de-software.svg?branch=master)](https://travis-ci.org/leticiamazzoportela/projeto-engenharia-de-software)

## Uso do Repositório

Serão um total de 4 entregas. Dessa forma, a cada entrega será criada uma tag indicando a versão atualizada.

### Estrutura do repositório

```
- src
   |- Código-Fonte

- PMO
   |- Documentos do projeto
```

## Ferramenta para Manutenção das Tarefas

Como forma de manter atualizado o status das tarefas, será utilizada a ferramenta ZenHub.
Esta é responsável por transformar as issues do GitHub em tarefas de desenvolvimento, sendo possível para os desenvolvedores controlar o andamento do cronograma.

Segue o link com instruções para a utilização da ferramenta: https://www.zenhub.com/

Para utilizá-la, basta instalar a extensão no navegador e estar como colaborador do repositório.

## Build do projeto

O build é realizado utilizando o pacote pyinstall, o qual pode ser instalado da seguinte forma:

```
pip install pyinstaller
```

Para realizar o build apenas utilize o comando:

```
pyinstaller —onefile src/interface.py
```
