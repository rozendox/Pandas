#!/usr/bin/env python
# coding: utf-8

# 
# 

# In[1]:


import pandas as pd


# In[2]:


#carrega arquivo para dataframe Pandas
dados = pd.read_csv("Credit.csv") 
#formato
dados.shape


# In[3]:


#resumo estatístico de colunas numéricas
dados.describe()


# In[4]:


#primeiros registros
dados.head()


# In[5]:


#últimos registros, com parâmetros
dados.tail(2)


# In[6]:


#filtras por nome da coluna
dados[["duration"]] 


# In[7]:


#filtrar linhas por indice
dados.loc[1:3]


# In[8]:


#linhas 1 e 3
dados.loc[[1,3]]


# In[9]:


#filtro
dados.loc[dados['purpose'] == "radio/tv"]


# In[10]:


#outra condição
dados.loc[dados['credit_amount'] >  18000]


# In[11]:


#atribuimos resultado a variável, criando outro df
credito2 = dados.loc[dados['credit_amount'] >  18000]
print(credito2)


# In[12]:


#definimos só algumas colunas
credito3 = dados[['checking_status','duration']].loc[dados['credit_amount'] >  18000]
print(credito3)


# In[13]:


#séries, única coluna
# pode ser criada a partir de listas, array do numpy ou coluna de data frame
s1 = pd.Series([2,5,3,34,54,23,1,16])
print(s1)


# In[14]:


#serie a partir de um array do numpy
import numpy as np
array1 = np.array([2,5,3,34,54,23,1,16])
s2 = pd.Series(array1)
print(s2)


# In[15]:


#series a partir de um dataframe
s3 = dados['purpose']
print(s3)
type(s3)


# In[16]:


#note a diferença, temos um data frame
d4= dados[['purpose']]
type(d4)


# In[17]:


#renomear
dados.rename(columns={"duration":"duração","purpose":"propósito"})


# In[18]:


#porém a alteração não é persistida
dados.head(1)


# In[19]:


#para persistir
dados.rename(columns={"duration":"duração","purpose":"propósito"},inplace=True)


# In[20]:


dados.head(1)


# In[21]:


#excluir coluna
dados.drop('checking_status',axis=1,inplace=True)
print(dados)


# In[22]:


dados.head(1)


# In[23]:


#verificar dados nulos
dados.isnull()


# In[24]:


#verificar dados nulos
dados.isnull().sum()


# In[25]:


#retirar colunas com NaN
dados.dropna()


# In[26]:


#preencher dados faltantes
dados['duração'].fillna(0,inplace = True)


# In[27]:


#iloc
dados.iloc[0:3,0:5]


# In[28]:


dados.iloc[[0,1,2,3,7],0:5]


# In[ ]:




