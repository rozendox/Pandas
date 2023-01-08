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

#resumo estatístico de colunas numéricas
dados.describe()

"""
output:

duration	credit_amount	installment_commitment	residence_since	age	existing_credits	num_dependents
count	1000.000000	1000.000000	1000.000000	1000.000000	1000.000000	1000.000000	1000.000000
mean	20.903000	3271.258000	2.973000	2.845000	35.546000	1.407000	1.155000
std	12.058814	2822.736876	1.118715	1.103718	11.375469	0.577654	0.362086
min	4.000000	250.000000	1.000000	1.000000	19.000000	1.000000	1.000000
25%	12.000000	1365.500000	2.000000	2.000000	27.000000	1.000000	1.000000
50%	18.000000	2319.500000	3.000000	3.000000	33.000000	1.000000	1.000000
75%	24.000000	3972.250000	4.000000	4.000000	42.000000	2.000000	1.000000
max	72.000000	18424.000000	4.000000	4.000000	75.000000	4.000000	2.000000


"""

#Trazendo os 5 primeiros registros
dados.head()

"""

	checking_status	duration	credit_history	                purpose	        credit_amount	        savings_status	employment	installment_commitment	personal_status	        other_parties	...	property_magnitude	age	other_payment_plans	housing	        existing_credits	job	                num_dependents	        own_telephone	foreign_worker	class
     0    <0	          6 	'critical/other existing credit'	radio/tv	   1169	        'no known savings'	>=7	                4	        'male single'	        none	...	        'real estate'	        67	        none	        own	        2	                 skilled	                1	        yes	        yes	        good
     1    0<=X<200  	  48	'existing paid'	                        radio/tv	   5951	                <100	        1<=X<4	                2	        'female div/dep/mar'	none	...	        'real estate'	        22	        none	        own	        1	                 skilled	                1	        none	        yes	        bad
     2	 'no checking'	  12	'critical/other existing credit'	education	   2096	                <100	        4<=X<7	                2	        'male single'	        none	...	        'real estate'	        49	        none	        own	        1	                'unskilled resident'	        2	        none	        yes	        good
     3	  <0	          42	'existing paid'	                    furniture/equipment    7882	                <100	        4<=X<7	                2	        'male single'	        guarantor	...	'life insurance'	45	        none	        'for free'	1	                 skilled	                2	        none	        yes	        good
     4	  <0	          24	'delayed previously'	                'new car'	   4870	                <100	        1<=X<4          	3	        'male single'	        none	...	        'no known property'	53	        none	        'for free'	2	                 skilled	                2	        none	        yes	        bad
5 rows × 21 columns     


"""
