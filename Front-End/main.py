import pandas as pd
import streamlit as st

# -------------------- INTERFACE --------------------
st.header('Automação para disparo de mensagens no WhatsApp')

st.markdown('''
        ##### **Siga o modelo abaixo para preencher sua planilha**, caso a planilha upada na ferramenta não esteja no formato correto os envios podem não ser concluídos.
''')

st.table({
    'Telefone': ['21999990000', '21900009999', '21911112222'],
    'Mensagem': ['Olá, tudo bem?', 'Olá, tudo bem?', 'Olá, tudo bem?']
})

# upload planilha
planilha = st.file_uploader(
    '**Faça aqui o upload da sua planilha** :arrow ',
    type=['.xlsx', '.csv']
)

if planilha:
  df = pd.read_excel(planilha)
  st.success('Planilha recebida!')