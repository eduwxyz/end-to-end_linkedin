# End-to-end Linkedin scraping

Este repositório tem como objetivo extrair dados do LinkedIn e montar um projeto completo de Engenharia de Dados. Aqui você encontrará ferramentas e códigos que lhe permitirão coletar informações valiosas do LinkedIn, processá-las e transformá-las em insights úteis para o seu projeto. Com esse projeto end-to-end, você terá acesso a uma ampla gama de ferramentas que estão em extrema alta em vagas para engenheiros de dados. Então, se você está procurando um projeto para iniciar ou aumentar seu portifólio e aprender ferramentas novas, este repositório é o lugar certo para começar.

# Motivação

A motivação para construir esse projeto, é para fornecer uma boa oportunidade para desenvolver habilidades e experiência em uma variedade de ferramentas. Como tal, o projeto é mais complexo do que o necessário, utilizando dbt, airflow, docker e armazenamento baseado em nuvem.

# Arquitetura

<img src="https://github.com/DevShy/end-to-end_linkedin/blob/main/imagens/pipeline.png" width=70% height=70%>

1. Extração dos dados utilizando a biblioteca scrapy;
2. Fazendo carregamento dos dados extraídos para o postgreSQL;
3. Fazer o carregamento dos dados para a Google Cloud Plataform;
4. Fazer transformações nos dados utilizando o dbt;
5. Para utilizar orquestração utilizaremos o Airflow e o Docker;
6. Criar dashboards utilizando o metabase.

# Output

Em construção...

# Configuração

Siga as etapas abaixo para configurar o pipeline:

Primeiro clone o repositório em seu diretório inicial e siga as etapas.

```
git clone https://github.com/DevShy/end-to-end_linkedin
cd end-to-end_linkedin_scraping
```

1. [Overview](instrucoes/overview.md)
1. [Poetry](instrucoes/poetry.md)
1. [Scrapy](instrucoes/scrapy.md)
