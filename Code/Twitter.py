#!/usr/bin/env python
# coding: utf-8

# # API DO TWITTER

# ### IMPORTANDO BIBLIOTECAS

# API do Twitter<br>
#     <font color='green'>import </font> tweepy<br>   
# Responsavel pela "espera". Faz com que um programa seja obrigado a aguardar os segundos determinados pelo sleep, para    poder executar o próximo código.<br>
#     <font color='green'>from </font> time<font color='green'> import</font> sleep<br>
#     
# Responsável pela fornecimento ao banco de dados de caracteres unicode.<br>
#     <font color='green'>import </font>unicodedata <br>
#     
# Usado como definição de hora atual (datetime.now).<br>
#     <font color='green'>from</font> datetime<font color='green'> import</font> datetime<br>
#     
# Utilizado para definir um horário especifico.
# <br>Pode somar a hora atual, com a quantidade de tempo (segudos,minutos,horas) desejado.
# <br>Exemplo: hora atual (17:08) + x horas determinadas pelo módulo(1 hora) = 18:08 <br>
#     <font color='green'>from</font> datetime <font color='green'>import </font>timedelta<br>
# 
# Define um número aleatório, entre os números impostos no parâmetro.<br>
# Exemplo: randint(0,5) - 
#     Ele escolherá um número entre 0 e 5.<br>
#     <font color='green'>from</font> random <font color='green'>import </font>randint<br>
# 
# O módulo "tqdm" mostra uma barra de progresso para o "for", em formato gráfico.<br>
# A cada laço executado ele demonstra sua taxa de tempo de execução.<br>
# Importante em casos de analise de scripts em relação a qualidade de processamento.<br>
#     <font color='green'>from </font>tqdm <font color='green'>import </font>tqdm<br>

# In[ ]:


import tweepy
from time import sleep
import unicodedata
from datetime import datetime
from datetime import timedelta
from random import randint
from tqdm import tqdm


# 
# ---------------------------------------------------------------------------------------------------------------------------

# ### CHAVES DO TWITTER
# 
# 
# ###### CHAVES UTILIZADAS PARA O ACESSO AS INFORMAÇÕES DO TWITTER.
# ESSA CHAVE É DISPONIBILIZADA PELA EMPRESA, PARA O ARMAZENAMENTO OU ANALISE DOS DADOS INFORMADOS PELA REDE SOCIAL.

# In[ ]:


ckey = ""
csecret = ""
atoken = ""
asecret = ""


# ###### DICIONARIO CRIADO COM AS CHAVES DO TWITTER

# In[ ]:


OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)


# -----------------------------------------------------------------------------------------------------------------------

# ### DADOS
# 
# 
# A execução desse código faz com que, seja aberta uma sessão para a criação de um CSV, com o nome de "Tweets.csv" e com apelido de " tl ".<br>
# O arquivo será salvo no mesmo caminho em que o código será executado.<br>
#     <font color='blue'> "with open('Tweets.csv','a') as tl:"</font><br>
# 
# Após a abertura dessa sessão, iremos criar a variavel "futuro". Essa variavel determina uma hora a mais em comparação ao horário atual.<br>
# O timedelta aceita a mudança de paramentro como "seconds, minutes e hours". Sendo possível personaliza-lo da forma que desejar.<br> 
#     <font color='blue'>"futuro = datetime.now() + timedelta(minutes=60)"</font><br>
# 
# Em seguida será executado um laço onde determina que, enquanto a hora atual for menor que a hora imposta no timedelta da variavel futuro (60 minutos ou 1 hora), será executado o restante do bloco.<br>
# Ou seja, enquanto não for atingido o tempo máximo determinado, o código estará em execução.<br>
#     <font color='blue'>"while datetime.now() < futuro:" </font><br>
# 
# Em cricTweet utilizamos a API do twitter, que realiza uma busca na rede social, baseando-se na "hashtag" determinada no código, sendo imposto um limite de 100 pesquisas a cada laço executado<br>
#     <font color='blue'>"cricTweet = tweepy.Cursor(api.search, q='#elenao').items(100)"</font> <br>
# 
# Sua sequência traz a variavel "numero", onde determina a escolha de um valor aleatório entre 5 e 30.<br>
# O "sleep" utiliza um valor determinado pela variavel "numero", onde são passados os parametros de quantos segundos o programa deverá "esperar", para poder dar continuidade ao código.<br>
# Resumindo, o programa irá aguarda de 5 a 30 segundos para ser executado novamente, simulando assim a pesquisa de uma pessoa comum.<br>
#     <font color='blue'>"numero = randint(5,30)<br>
#         sleep(numero)" </font><br>
#         
# O laço "for" irá fazer com que a cada vez que seja feita uma pesquisa no Twitter ele pegue informações determinadas dentro do laço. <br>
# O tqdm mostrará de forma gráfica uma barra de progresso para sabermos quanto tempo o "for" irá levar para ser executado por completo.<br>
#     <font color='blue'>" for tweet in tqdm(cricTweet):" </font><br>
# 
# 
# Explicação das variaveis:<br>
# ***data***: Essa variavel é responsavel por trazer a informação da criação do texto postado no Twitter.<br>
#     <font color='blue'>"data = tweet.created_at " </font><br>
# 
# ***texto***: É responsavel pelos textos escritos em um determinado tweet.<br>
# O ".encode" terá a funcionalidade de transformar alguns caractéres especiais, que não podem ser lidos por um csv.<br>
# O "replace" irá substituir a quebra de linhas utilizadas nos textos por um "pipe" ou barra vertical ( | ), dessa forma o texto ao ser importado para um csv, poderá manter sua tabulação correta, estando sempre na coluna desejada.<br>
#     <font color='blue'>"texto = tweet.text.encode('ascii','ignore').replace("\n", " | ") " </font><br>
# 
# ***lingua***: Como o nome já diz, a variavel informa em qual linguagem foi criado o tweet.<br>
#     <font color='blue'>" lingua = tweet.lang " </font><br>
# 
# Na sequencia a variavel "data" será formatada, mantendo-se como uma string e passando os parametros para poder criar uma mascara.<br>
# ***%Y:***  Ano<br>
# ***%m:***  Mês<br>
# ***%d:***  Dia<br>
# ***%H:***  Hora<br>
# ***%M:***  Minuto<br>
# ***%S:***  Segundo<br>
# ***%Z:***  É o horário UTC(Tempo Universal Coordenado), em outras palavras, um deslocamento de 0, equivalente a "2018-11-11 12:22:09.144 + 0:00<br>
#     <font color='blue'>"data = datetime.strftime(data,"%Y-%m-%d %H:%M:%S %Z") " </font><br>
# 
# Por ultimo iremos utilizar o csv que nomeamos como "tl" e iremos escrever todas as informações descritas anteriormente.<br>
# Data mais um delimitador ponto e vírgula (;) que é aceito em csv, o texto e o delimitador, a lingua em que foi criado a postagem e por fim uma quebra de linha.<br>
# Dessa forma ele cria um arquivo, com as informações resgatadas, montando uma tabela ou planilha.<br>
#     <font color='blue'>"tl.write(data + ";" + texto + ";" + lingua+"\n")   " </font><br>
# 

# In[ ]:


with open('Tweets.csv','a') as tl:
    futuro = datetime.now() + timedelta(minutes=60)
    while datetime.now() < futuro:
        
        
        cricTweet = tweepy.Cursor(api.search, q='#elenao').items(100)
        
        numero = randint(5,30)
        sleep(numero)
        
        for tweet in tqdm(cricTweet):
            data = tweet.created_at
            texto = tweet.text.encode('ascii','ignore').replace("\n", " | ")
            lingua = tweet.lang
            data = datetime.strftime(data,"%Y-%m-%d %H:%M:%S %Z")
            tl.write(data + ";" + texto + ";" + lingua+"\n")  


# ### Considerações Finais
# 
# Esse código foi feito em Python 2.7.15. Utilizando uma "máquina virtual" no Anaconda Navigator;
# 
# Para a execução do código, instale as bibliotecas descritas na primeira pagina;
# 
# As chaves do Twitter, informadas na segunda página, não deverão ser divulgadas;
# 
# Dependendo da "hashtag" utilizada, o arquivo pode variar de tamanho, ou seja, pode ser que haja muitas informações divulgadas, ou nenhuma informação;
# 
# Caso queira um teste rápido, altere o valor de "timedelta(minutes=60)".<br>
# Exemplo: timedelta(seconds=60) - Acrescentando 60 segundos a hora atual;
# 
# A utilização da "hashtag" no código é apenas ilustrativa.<br>
# Devido a grande repercução, utilizei a mesma para coletar um grande número de dados, em menos tempo possível;
