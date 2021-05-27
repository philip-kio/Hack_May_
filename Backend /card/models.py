
from django.db import models
from autoslug import AutoSlugField
from shortuuidfield import ShortUUIDField
from django_unique_slugify import unique_slugify
import uuid

# Create your models here.


class CardDetail(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length= 25)
    uuid= models.UUIDField(default=uuid.uuid4,max_length=2, help_text= 'Unique ID for each card')
    slug = models.SlugField()
    employment_title = models.CharField(max_length=40)
    company =  models.CharField(max_length=45)
    email = models.EmailField()
    brief_description = models.TextField()
    linkedIn = models.URLField()

    def save(self,**kwargs):
        uuid_str = str(self.uuid)
        slug_str = f'{self.slug}-{uuid_str[:6]}'
        unique_slugify(self,slug_str)
        super(CardDetail, self).save(**kwargs)

    def __str__(self):
        return self.first_name
