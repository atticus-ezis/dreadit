import pandas as pd
from datetime import datetime

reader = pd.read_excel('/Users/atticusezis/coding/dreadit/dreadit/creepypastas.xlsx')
df = pd.DataFrame(reader)

# data type for tags = <class 'str'>
# print(type(df['tags'].iloc[0]))

# # data type for categories = <class 'str'> 
# print(type(df['categories'].iloc[0]))

# init_tags = df['tags'].iloc[0]
# tag_array = [tag.strip() for tag in init_tags.split(',')]

# print(df['tags'].iloc[0])

sample_tags = df['tags'].iloc[0:50]



['drug trials', 'drugs', 'experimentation', 
 'experiments', 'madness', 'Peter Frost David', 
 'psychological', 'psychological horror', 'sci-fi', 
 'science', 'science fiction', 'time']

# irregular_tag = df[df['story_name']=='The Dognapper'].iloc[0]
# irregular_tag_items = irregular_tag['tags'].split('\n')


def find_author(tag_list):
        tags_to_remove = ['Video Narratives OK', 'WatchThe-Aftermath', 'Bedtime Series']
        cleaned_tags = [tag for tag in tag_list if tag not in tags_to_remove]

        for tag_item in cleaned_tags:

            if tag_item == 'anonymously authored':
                return 'Unkown'

            if tag_item[0] == tag_item[0].upper():
                return tag_item
            
        return 'Unkown'
                
# AttributeError: 'float' object has no attribute 'split'


def seperate_tags(sample_tags):
    authors = []
    for tag_row in sample_tags:

        if isinstance(tag_row, str):
            tag_list = [tag.strip() for tag in tag_row.split(',')]
            author = find_author(tag_list)
            authors.append(author)

        else:
            print(f"Non-string tag_row found: {tag_row} (type: {type(tag_row)})")
    

    return authors 

test_seperate_tags = seperate_tags(sample_tags)
print(test_seperate_tags)
                 
            

