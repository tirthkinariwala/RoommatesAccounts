import pandas as pd

df = pd.read_excel('output2.xlsx', index_col=0)
d2 = pd.read_csv('\\\\AURORA\\Users\\Public\\Documents\\Accounts 2020\\Categories.csv', header=None, index_col=0, squeeze=True).to_dict()
# d2 = {key: dep for key, dep in zip(d['Keyword'], d['Department'])}

def mapper(x):
    return d2.get(next((i for i in d2 if i.lower() in x.lower()), None))

df['Category'] = df['Location'].apply(mapper).apply(pd.Series)

df.to_excel("Check.xlsx")