import pandas as pd
import urllib
import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def armazenar_planilha(lista):
  df = pd.read_excel(lista)
  return df
# ------------------------------ INTERFACE ------------------------------
st.header('Automação para disparo  WhatsApp')

with st.form(key='disparo', clear_on_submit=True):
  mensagem = st.text_area('**Insira a mensagem que deseja disparar em massa:**', placeholder='Ola, tudo bem? \n\nSeja bem-vindo a ...')
  planilha = st.file_uploader(
    '**Faça aqui o upload da sua planilha:**',
    type=['.xlsx', '.csv']
  )
  aceito_termos = st.checkbox('**Aceito os termos de uso dessa automação.**')
  enviar = st.form_submit_button('**Enviar informações**', type='primary')

if enviar == True:
  if mensagem and planilha and aceito_termos:
    
    st.success('Informações enviadas com sucesso.')
  else:
    st.warning('Preencha todos os campos corretamente.')


# ------------------------------ BACK-END ------------------------------


# # tratando a base de dados
# # removendo as colunas desnecessárias
# df.drop('Nome:', axis=1, inplace=True)
# df.drop('rating', axis=1, inplace=True)

# # criando colunas
# df['Mensagem:'] = 'Olá, tudo bem?'

# tratando caracteres especiais
# df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace('+', ''))
# df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace(' ', ''))
# df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace('-', ''))
# df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace('(', ''))
# df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace(')', ''))

# # adicionando o código do país nos números que não tem
# df['Telefone:'] = df['Telefone:'].apply(lambda x: '55' + x if '55' not in x else x)



# # # separando em lista menores com 50 números
# # # df1 = df[7:51]
# # # df2 = df[51:101]
# # # df3 = df[101:]

# #-------------------- TRABALHANDO COM SELENIUM --------------------
# # abrindo o navegador e acessando o site
# navegador = webdriver.Chrome()
# navegador.get('https://web.whatsapp.com/')
# while len(navegador.find_elements(By.ID, 'side')) < 1:
#   time.sleep(1)
# time.sleep(2)

# navegador.minimize_window()

# for linha in df.index:
#     mensagem = df.loc[linha, 'Mensagem:']
#     telefone = df.loc[linha, 'Telefone:']

#     # convertendo a mensagem para linguagem da api do link
#     texto = urllib.parse.quote(mensagem)
    
#     # gerando o link com telefones e a mensagem
#     link = f'https://web.whatsapp.com/send?phone={telefone}&text={texto}'

#     # abrindo o link criado para enviar a mensagem
#     navegador.get(link)
    
#     # aguardar a página carregar
#     while len(navegador.find_elements(By.ID, 'side')) < 1:
#       time.sleep(1)
#     time.sleep(2)

#     # enviar a mensagem
#     navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
#     time.sleep(8)
