import pandas as pd
from models import Tag, Story, Category, ReadingTime
from datetime import datetime

df = pd.read_excel('creepypastas.xlsx')


for row in df.itertuples(index=False):
    story = Story.objects.create(
        story_name = row.story_name,
        body = row.body,
        creepypasta_rating = row.average_rating,
        native_story = False,
    )

    # create tag object and add to story 
    tag_names = [tag.strip() for tag in (row.tags or '').split(',')]
    for tag_name in tag_names:
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        story.tags.add(tag)

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
    


