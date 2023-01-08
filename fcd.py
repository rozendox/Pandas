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


#Trazendo os últimos registros, com parâmetros
dados.tail(2)

"""
output:

checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
998	<0	45	'existing paid'	radio/tv	1845	<100	1<=X<4	4	'male single'	none	...	'no known property'	23	none	'for free'	1	skilled	1	yes	yes	bad
999	0<=X<200	45	'critical/other existing credit'	'used car'	4576	100<=X<500	unemployed	3	'male single'	none	...	car	27	none	own	1	skilled	1	none	yes	good

"""


#Filtrar por nome da coluna
dados[["duration"]] 


""" 
output:

duration
0	6
1	48
2	12
3	42
4	24
...	...
995	12
996	30
997	12
998	45
999	45
1000 rows × 1 columns

"""


#filtrar linhas por indice
dados.loc[1:3]


"""
output:

checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
1	0<=X<200	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	...	'real estate'	22	none	own	1	skilled	1	none	yes	bad
2	'no checking'	12	'critical/other existing credit'	education	2096	<100	4<=X<7	2	'male single'	none	...	'real estate'	49	none	own	1	'unskilled resident'	2	none	yes	good
3	<0	42	'existing paid'	furniture/equipment	7882	<100	4<=X<7	2	'male single'	guarantor	...	'life insurance'	45	none	'for free'	1	skilled	2	none	yes	good

"""

#linhas 1 e 3
dados.loc[[1,3]]


"""
output:

checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
1	0<=X<200	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	...	'real estate'	22	none	own	1	skilled	1	none	yes	bad
3	<0	42	'existing paid'	furniture/equipment	7882	<100	4<=X<7	2	'male single'	guarantor	...	'life insurance'	45	none	'for free'	1	skilled	2	none	yes	good

"""


#filtro
dados.loc[dados['purpose'] == "radio/tv"]


"""
output:

	checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
0	<0	6	'critical/other existing credit'	radio/tv	1169	'no known savings'	>=7	4	'male single'	none	...	'real estate'	67	none	own	2	skilled	1	yes	yes	good
1	0<=X<200	48	'existing paid'	radio/tv	5951	<100	1<=X<4	2	'female div/dep/mar'	none	...	'real estate'	22	none	own	1	skilled	1	none	yes	bad
8	'no checking'	12	'existing paid'	radio/tv	3059	>=1000	4<=X<7	2	'male div/sep'	none	...	'real estate'	61	none	own	1	'unskilled resident'	1	none	yes	good
12	0<=X<200	12	'existing paid'	radio/tv	1567	<100	1<=X<4	1	'female div/dep/mar'	none	...	car	22	none	own	1	skilled	1	yes	yes	good
15	<0	24	'existing paid'	radio/tv	1282	100<=X<500	1<=X<4	4	'female div/dep/mar'	none	...	car	32	none	own	1	'unskilled resident'	1	none	yes	bad
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
989	0<=X<200	24	'critical/other existing credit'	radio/tv	1743	<100	>=7	4	'male single'	none	...	'life insurance'	48	none	own	2	'unskilled resident'	1	none	yes	good
991	'no checking'	15	'all paid'	radio/tv	1569	100<=X<500	>=7	4	'male single'	none	...	car	34	bank	own	1	'unskilled resident'	2	none	yes	good
992	<0	18	'existing paid'	radio/tv	1936	'no known savings'	4<=X<7	2	'male mar/wid'	none	...	car	23	none	rent	2	'unskilled resident'	1	none	yes	good
997	'no checking'	12	'existing paid'	radio/tv	804	<100	>=7	4	'male single'	none	...	car	38	none	own	1	skilled	1	none	yes	good
998	<0	45	'existing paid'	radio/tv	1845	<100	1<=X<4	4	'male single'	none	...	'no known property'	23	none	'for free'	1	skilled	1	yes	yes	bad


"""


#outra condição
dados.loc[dados['credit_amount'] >  18000]

"""
output:


checking_status	duration	credit_history	purpose	credit_amount	savings_status	employment	installment_commitment	personal_status	other_parties	...	property_magnitude	age	other_payment_plans	housing	existing_credits	job	num_dependents	own_telephone	foreign_worker	class
915	0<=X<200	48	'no credits/all paid'	other	18424	<100	1<=X<4	1	'female div/dep/mar'	none	...	'life insurance'	32	bank	own	1	'high qualif/self emp/mgmt'	1	yes	no	bad

"""


#atribuimos resultado a variável, criando outro df
credito2 = dados.loc[dados['credit_amount'] >  18000]
print(credito2)


"""
output:

    checking_status  duration         credit_history purpose  credit_amount  \
915        0<=X<200        48  'no credits/all paid'   other          18424   

    savings_status employment  installment_commitment       personal_status  \
915           <100     1<=X<4                       1  'female div/dep/mar'   

    other_parties  ...  property_magnitude age  other_payment_plans housing  \
915          none  ...    'life insurance'  32                 bank     own   

    existing_credits                          job num_dependents  \
915                1  'high qualif/self emp/mgmt'              1   

     own_telephone foreign_worker class  
915            yes             no   bad  

[1 rows x 21 columns]
"""

#definimos só algumas colunas
credito3 = dados[['checking_status','duration']].loc[dados['credit_amount'] >  18000]
print(credito3)

"""
    checking_status  duration
915        0<=X<200        48

"""

