import pandas as pd
import streamlit as st

def armazenar_planilha(lista):
  df = pd.read_excel(lista)
  return df
# -------------------- INTERFACE --------------------
st.header('Automação para disparo de mensagens no WhatsApp')

st.markdown('''
        ##### Faça upload da planilha contendo apenas uma coluna com os telefones que deseja disparar as mensagens. Siga o modelo abaixo para preencher sua planilha.
''')

st.dataframe({
    'Telefone': ['21999990000', '21900009999', '21911112222'],
})

mensagem = st.text_input(
  '**Insira a mensagem que deseja disparar em massa:**',

  )

# upload planilha
planilha = st.file_uploader(
    '**Faça aqui o upload da sua planilha:**',
    type=['.xlsx', '.csv']
)

if planilha and mensagem:
  result = st.button('Enviar', type='primary')
  on_click=armazenar_planilha(planilha)
  df = armazenar_planilha(planilha)
  df['Mensagem teste:'] = mensagem
  imprimir = st.dataframe(df)
else:
  st.warning('Preencha todos os campos.')