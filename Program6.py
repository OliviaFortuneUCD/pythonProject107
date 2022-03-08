import pandas as pd

from datetime import date

df = pd.DataFrame({
    'name': ['alice','bob','charlie'],
    'date_of_birth': ['25/10/2005','29/10/2002','01/01/2001']
})

df['date_of_birth'] = pd.to_datetime(df['date_of_birth'],format='%d/%m/%Y')


df1 = df[
    (df['date_of_birth'] > '25/10/2002' ) &
    (df['date_of_birth'] < '25/10/2006')
]

print(df1)