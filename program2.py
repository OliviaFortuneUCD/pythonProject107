import pandas as pd

df = pd.DataFrame({
    'name': ['alice','bob','charlie'],
    'date_of_birth': ['27/05/2001','16/02/1999','25/09/1998']
})

df['date_of_birth'] = pd.to_datetime(df['date_of_birth'],format='%d/%m/%Y')
print(df['date_of_birth'])