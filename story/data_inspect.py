import pandas as pd

reader = pd.read_excel('/Users/atticusezis/coding/dreadit/dreadit/creepypastas.xlsx')
df = pd.DataFrame(reader)

# data type for tags = <class 'str'>
print(type(df['tags'].iloc[0]))

# data type for categories = <class 'str'> 
print(type(df['categories'].iloc[0]))

init_tags = df['tags'].iloc[0]
tag_array = [tag.strip() for tag in init_tags.split(',')]

print(df['tags'].iloc[0])