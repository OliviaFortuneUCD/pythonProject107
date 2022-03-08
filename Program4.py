import pandas as pd
from datetime import datetime

df = pd.DataFrame({
    "name":["alice","bob","charlie", "david"],
    "age":[12,43,22,34]
})

# a timestamp column
df["timestamp_col"] = pd.Timestamp(datetime.now())

# use strftime to turn a timestamp into a
# a nicely formatted d-m-Y string:
df["formatted_col"] = df["timestamp_col"].map(lambda ts: ts.strftime("%d-%m-%Y"))
print(df)