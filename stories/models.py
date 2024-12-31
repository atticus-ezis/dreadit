from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='author_profiles/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) # urls identifier  
    content = models.TextField
    author = models.ForeignKey('Author', on_delete = models.CASCADE, related_name="stories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0.0)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tags', related_name="stories", blank=True) #myTag.stories.all()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name