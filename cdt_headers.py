import pandas as pd
df=pd.read_csv("C:\python/cdt.txt", sep='\t')
headers=["date", "time (in s)", "depth (in m)", "T (in degC)", "salinity (in psu)"]
df.columns=headers
print(df)
