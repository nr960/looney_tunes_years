import pandas as pd

df1 = pd.read_csv('1944-1964 - CHARACTERS.csv')
df2 = pd.read_csv('1944-1964 - YEARS.csv')

for col in df1.select_dtypes(include=['object']).columns:
    df1[col] = df1[col].str.strip(' *C')

for col in df2.select_dtypes(include=['object']).columns:
    df2[col] = df2[col].str.strip(' *')

print(df2['Y_1948'])
print(df1['BUGS'])