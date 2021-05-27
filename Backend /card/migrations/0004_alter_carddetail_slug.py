# Generated by Django 3.2.3 on 2021-05-26 15:53

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_alter_carddetail_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetail',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=25)),
        ),
    ]