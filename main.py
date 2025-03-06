import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os

# Função para criar conexão com o banco de dados
def get_db_connection():
    # Buscar a variável de ambiente DATABASE_URL diretamente do sistema
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL is None:
        raise ValueError("Erro: DATABASE_URL não encontrada nas variáveis de ambiente.")
    try:
        engine = create_engine(DATABASE_URL)
        return engine
    except Exception as e:
        raise Exception(f"Erro ao conectar ao banco de dados: {e}")

# Título da aplicação
st.title("Upload de Arquivo CSV")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Leitura do arquivo CSV
    df = pd.read_csv(uploaded_file)
    st.write("Estrutura do Dataset:")
    st.write(df.head())

    # Conectar ao banco de dados
    try:
        engine = get_db_connection()
        st.success("Conexão com o banco de dados estabelecida com sucesso!")
    except Exception as e:
        st.error(str(e))
        st.stop()  # Interrompe a execução se houver erro na conexão

    # Criar tabela no banco de dados
    try:
        df.to_sql('temperature_logs', engine, if_exists='replace', index=False)
        st.success("Tabela criada com sucesso!")
    except Exception as e:
        st.error(f"Erro ao criar tabela: {e}")

    # Ler dados do banco de dados
    try:
        query = "SELECT * FROM temperature_logs"
        data = pd.read_sql(query, engine)
        st.write("Dados lidos com sucesso:")
        st.write(data.head())
    except Exception as e:
        st.error(f"Erro ao ler dados do banco de dados: {e}")

    # Visualização dos dados com Plotly
    st.title("Visualização dos Dados")
    try:
        fig = px.line(data, x='noted_date', y='temp', title='Série Temporal de Temperaturas')
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Erro ao gerar gráfico: {e}")