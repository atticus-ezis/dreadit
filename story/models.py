from django.db import models
import pandas as pd

excel_data = pd.read_excel('creepypastas.xlsx')
df = pd.DataFrame(excel_data)
mean_rating = df['average_rating'].mean()
print(mean_rating)

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __init__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __init__(self):
        return self.name
    

class Story(models.Model):
    story_name = models.CharField(max_length=250)
    # add author
    publish_date = models.DateField()
    creepypasta_rating = models.FloatField()
    native_rating = models.FloatField(null=True, blank=True)
    body = models.TextField()
    native_story = models.BooleanField()

    # many to many fields
    categories = models.ManyToManyField(Category, related_name='stories')
    tags = models.ManyToManyField(Tag, related_name='stories')

    
    # calculations 
    reading_time = models.CharField(max_length=20, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_body = self.body
        
    def find_reading_time(self):
        char_count = len(self.body) 
        if char_count < 250:
            return '1 min'
        elif char_count <= 250 * 15:
            return '1-15 min'
        elif char_count <= 250 * 30:
            return '15-30 min'
        elif char_count <= 250 * 60:
            return '30-60 min'
        else:
            return '60+ min'
        
    def save(self, *args, **kwargs):
        if not self.reading_time or self.original_body != self.body:
            self.reading_time = self.find_reading_time()
        super().save(*args, **kwargs)
        self.original_body = self.body

    def __str__(self):
        return self.story_name

    
    

        #  #   Column                  Non-Null Count  Dtype  
        # ---  ------                  --------------  -----  
        # 0   story_name              3510 non-null   object 
        # 1   average_rating          3510 non-null   float64
        # 2   tags                    2081 non-null   object 
        # 3   body                    3510 non-null   object 
        # 4   estimated_reading_time  3509 non-null   object 
        # 5   publish_date            3510 non-null   object 
        # 6   categories              3509 non-null   object 