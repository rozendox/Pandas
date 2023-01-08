#importanto a biblioteca pandas

import pandas as pd


#carrega arquivo para dataframe Pandas
dados = pd.read_csv("Credit.csv") 

#formato
dados.shape

"""
output:
        (1000, 21)
        
"""
