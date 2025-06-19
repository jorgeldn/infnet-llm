import streamlit as st
from agent import recomendar_pc

st.set_page_config(page_title="Assistente de Montagem de PC", layout="centered")
st.title("🖥️ Assistente de Montagem de PC")

proposito = st.text_input("Para qual finalidade você precisa do computador?")

if st.button("Gerar Recomendação"):
    if proposito.strip():
        with st.spinner("Pensando na melhor configuração..."):
            recomendacao = recomendar_pc(proposito)
            st.markdown("### 💡 Recomendação:")
            st.success(recomendacao)
    else:
        st.warning("Por favor, informe o propósito de uso.")
