import pandas as pd
import matplotlib.pyplot as plt
import tweepy

# Autenticação na API do Twitter
consumer_key = 'sua_consumer_key'
consumer_secret = 'sua_consumer_secret'
access_token = 'seu_access_token'
access_token_secret = 'seu_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Criando o objeto da API
api = tweepy.API(auth)

# Buscando tweets
query = 'python'
tweets = tweepy.Cursor(api.search_tweets, q=query).items(100)

# Criando um dicionário para armazenar a contagem de tweets por idioma
languages_count = {}

for tweet in tweets:
    lang = tweet.lang
    if lang in languages_count:
        languages_count[lang] += 1
    else:
        languages_count[lang] = 1

# Criando um dataframe com os dados
df = pd.DataFrame.from_dict(languages_count, orient='index', columns=['count'])

# Criando um gráfico de barras
plt.bar(df.index, df['count'])
plt.title('Contagem de tweets por idioma')
plt.xlabel('Idioma')
plt.ylabel('Contagem')
plt.show()
