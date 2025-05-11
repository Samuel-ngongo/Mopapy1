import streamlit as st
import numpy as np
import pandas as pd
from inteligencia import analisar_dados, estimar_proxima_rodada, avaliar_tendencia

st.set_page_config(page_title="Previsão Aviator", layout="centered")
st.title("Previsão Inteligente - Aviator")
st.markdown("Palavra-chave: **Aviator1**")

st.header("Inserção de Dados")
dados_input = st.text_area("Cole aqui os valores das rodadas (ex: 1.23x, 2.56x, 5.21x...)", height=150)
botao_analisar = st.button("Analisar Dados")

if 'historico' not in st.session_state:
    st.session_state.historico = []

if dados_input:
    try:
        dados_lista = [float(x.lower().replace("x", "").strip()) for x in dados_input.split(",") if x.strip()]
        st.session_state.historico.extend(dados_lista)
    except ValueError:
        st.error("Erro: Certifique-se de que todos os dados estão no formato correto, como 1.23x ou 2.56x")

if botao_analisar and st.session_state.historico:
    dados = st.session_state.historico[-50:]  # considera as últimas 50 rodadas
    st.subheader("Estatísticas Gerais")
    st.write(f"Rodadas analisadas: {len(dados)}")
    st.write(f"Média geral: {np.mean(dados):.2f}x")
    st.write(f"Desvio padrão: {np.std(dados):.2f}x")
    st.write(f"Maior valor: {max(dados):.2f}x")
    st.write(f"Menor valor: {min(dados):.2f}x")

    st.subheader("Estimativas Futuras")
    minimo, media_estimada = estimar_proxima_rodada(dados)
    st.write(f"Próxima rodada mínima provável: **{minimo:.2f}x**")
    st.write(f"Próxima rodada média estimada: **{media_estimada:.2f}x**")

    st.subheader("Tendência Atual")
    tendencia = avaliar_tendencia(dados)
    st.write(tendencia)

    st.subheader("Análise Inteligente")
    alertas = analisar_dados(dados)
    for alerta in alertas:
        st.warning(alerta)

st.divider()
st.subheader("Histórico Completo")
if st.session_state.historico:
    st.write([f"{v:.2f}x" for v in st.session_state.historico])

if st.button("Limpar Histórico"):
    st.session_state.historico = []
    st.success("Histórico limpo com sucesso!")