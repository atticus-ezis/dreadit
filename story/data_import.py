import pandas as pd
from models import Tag, Story, Category, ReadingTime
from datetime import datetime

reader = pd.read_excel('creepypastas.xlsx')
df = pd.DataFrame(reader)

for row in reader:
    story = Story.objects.create(
        story_name = row['story_name'],
        body = row['body'],
        creepypasta_rating = row['average_rating'],
        native_story = False,
    )

    # create tag object and add to story 
    tag_names = [tag.strip() for tag in row.get('tags', '').split(',')]
    for tag_name in tag_names:
        tag, _ = Tag.objects.get_or_create(tag_name)
        story.tags.add(tag)

    # create category object and add to story 
    category_names = [category.strip() for category in row['categories', ''].split(',')]
    for category_name in category_names:
        category = Category.objects.get_or_create(category_name)
        story.categories.add(category)

    # add date time
    date_str = row['publish_date']
    try:
        date_obj = datetime.strptime(row['publish_date'], '%B %d, %Y').date()
    except (ValueError, TypeError):
        date_obj = None
    story.publish_date = date_obj
    


