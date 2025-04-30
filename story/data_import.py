import pandas as pd
from models import Tag, Story, Category, ReadingTime
from datetime import datetime

df = pd.read_excel('creepypastas.xlsx')

def find_author(tag_list):
    tags_to_remove = ['Video Narratives OK', 'WatchThe-Aftermath', 'Bedtime Series']
    cleaned_tags = [tag for tag in tag_list if tag not in tags_to_remove]

    for tag_item in cleaned_tags:

        if tag_item == 'anonymously authored':
                return 'Unkown'
        if tag_item[0] == tag_item[0].upper():
                return tag_item
        
    return 'Unkown'

for row in df.itertuples(index=False):
    story = Story.objects.create(
        story_name = row.story_name,
        body = row.body,
        creepypasta_rating = row.average_rating,
        native_story = False,
    )

    # list tags, extract author, create Tag object, add to Story object
    if row.tags:
        tag_names = [tag.strip() for tag in (row.tags or '').split(',')]
        tags_to_remove = ['Video Narratives OK', 'WatchThe-Aftermath', 'Bedtime Series']
        cleaned_tags = [tag for tag in tag_names if tag not in tags_to_remove]


        story.author = find_author(tag_names)

        for tag_name in tag_names:
            if tag_name != story.author:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                story.tags.add(tag)
    else:
        story.author = "Unkown"

    # create category object and add to story 
    category_names = [category.strip() for category in (row.categories or '').split(',')]
    for category_name in category_names:
        category, _ = Category.objects.get_or_create(name=category_name)
        story.categories.add(category)

    # add date time
    date_str = (row.publish_date or '').strip()
    try:
        date_obj = datetime.strptime(date_str, '%B %d, %Y').date()
    except (ValueError, TypeError):
        date_obj = None
    story.publish_date = date_obj



    story.save()
    


