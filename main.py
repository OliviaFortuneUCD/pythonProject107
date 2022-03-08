import pandas as pd

df = pd.DataFrame({
    'name': ['alice','bob','charlie'],
    'date_of_birth': ['10/25/2005','10/29/2002','01/01/2001']
})
#You have to convert the datw into date time
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])
print(df['date_of_birth'])