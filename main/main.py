import pandas as pd
import urllib
import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# -------------------- CRIANDO FUNCTIONS --------------------
def enviarMensagens(dataFrame):
    for linha in dataFrame:
        mensagem = dataFrame.loc[linha, 'Mensagem:']
        telefone = dataFrame.loc[linha, 'Telefone:']
        texto = urllib.parse.quote(mensagem)
        link = f'https://web.whatsapp.com/send?phone={telefone}&text={texto}'
        return link
        # navegador.get(link)
        # while len(navegador.find_elements(By.ID, 'side')) < 1:
        #     time.sleep(1)
        # time.sleep(5)
        # if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        #     navegador.find_element(
        #         By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        # time.sleep(3)


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


# # tratando a base de dados
# # removendo as colunas desnecessárias
# df.drop('Nome:', axis=1, inplace=True)
# df.drop('rating', axis=1, inplace=True)

# # criando colunas
# df['Mensagem:'] = 'Olá, tudo bem?'

# tratando caracteres especiais
df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace('+', ''))
df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace(' ', ''))
df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace('-', ''))
df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace('(', ''))
df['Telefone:'] = df['Telefone:'].apply(lambda x: str(x).replace(')', ''))

# adicionando o código do país nos números que não tem
df['Telefone:'] = df['Telefone:'].apply(lambda x: '55' + x if '55' not in x else x)



# # separando em lista menores com 50 números
# # df1 = df[7:51]
# # df2 = df[51:101]
# # df3 = df[101:]

#-------------------- TRABALHANDO COM SELENIUM --------------------
# abrindo o navegador e acessando o site
navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')
while len(navegador.find_elements(By.ID, 'side')) < 1:
  time.sleep(1)
time.sleep(2)

navegador.minimize_window()

for linha in df.index:
    mensagem = df.loc[linha, 'Mensagem:']
    telefone = df.loc[linha, 'Telefone:']

    # convertendo a mensagem para linguagem da api do link
    texto = urllib.parse.quote(mensagem)
    
    # gerando o link com telefones e a mensagem
    link = f'https://web.whatsapp.com/send?phone={telefone}&text={texto}'

    # abrindo o link criado para enviar a mensagem
    navegador.get(link)
    
    # aguardar a página carregar
    while len(navegador.find_elements(By.ID, 'side')) < 1:
      time.sleep(1)
    time.sleep(2)

    # enviar a mensagem
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    time.sleep(8)
