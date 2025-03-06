# Projeto: Análise de Dados com Streamlit, PostgreSQL e Plotly

Este projeto foi desenvolvido como parte da disciplina **Disruptive Architectures: IOT, Big Data & IA** na **UniFECAF**. O objetivo é criar uma aplicação web para análise de dados, utilizando tecnologias como **Streamlit**, **PostgreSQL** e **Plotly**.

## 📝 Descrição do Projeto

O projeto consiste em uma aplicação web que permite o upload de arquivos CSV contendo dados de temperatura. Os dados são armazenados em um banco de dados PostgreSQL e visualizados em gráficos interativos utilizando a biblioteca Plotly. A aplicação foi desenvolvida em Python e está hospedada no Render.

## 🚀 Funcionalidades

- **Upload de arquivos CSV:** A aplicação permite o upload de arquivos CSV contendo dados de temperatura.
- **Armazenamento em banco de dados:** Os dados são armazenados em um banco de dados PostgreSQL.
- **Visualização de dados:** Os dados são exibidos em uma tabela e em um gráfico interativo de séries temporais.
- **Gráficos interativos:** Utilização do Plotly para criar gráficos interativos e responsivos.

## 🛠️ Tecnologias Utilizadas

- **Streamlit:** Para criação da interface web.
- **PostgreSQL:** Para armazenamento dos dados.
- **Plotly:** Para criação de gráficos interativos.
- **Python:** Linguagem de programação principal.
- **Render:** Para hospedagem da aplicação.

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina as seguintes ferramentas:
- **Python** (versão 3.8 ou superior)
- **Poetry** (para gerenciamento de dependências)
- **PostgreSQL** (ou um banco de dados remoto)

## 🛠️ Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Nathali-Cardoso/iot-pipeline-de-dados
   cd iot-pipeline-de-dados

2. **Instale as dependências:**
   ```bash
   poetry install

3. **Configure o banco de dados:**
  ```bash
   DATABASE_URL=postgresql://usuario:senha@host:porta/nome_do_banco

4. **Execute a aplicação:**
   ```bash
   poetry run streamlit run main.py


## 🚀 Deploy no Render

A aplicação está hospedada no Render. Você pode acessá-la através do seguinte link:
https://iot-pipeline-de-dados.onrender.com


## 📊 Exemplo de Uso

1. Upload de arquivo CSV:

   Faça upload de um arquivo CSV contendo dados de temperatura.

   A aplicação exibirá os dados em uma tabela e gerará um gráfico interativo.

2. Visualização de dados:

   Os dados são armazenados no banco de dados PostgreSQL e podem ser visualizados em um gráfico de séries temporais.


## 📝 Licença

Este projeto foi desenvolvido como parte de um trabalho acadêmico e não possui uma licença específica. O código pode ser utilizado para fins educacionais, mas não para uso comercial.

Feito com ❤️ por Nathali Cardoso