import pandas as pd

df = pd.read_csv('test.csv', encoding='utf-8-sig')
authors = set(df['authors'])
print authors