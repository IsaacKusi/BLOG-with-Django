# Generated by Django 4.1.7 on 2023-04-07 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0005_alter_blogposts_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='date_published',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 7, 10, 43, 47, 160240, tzinfo=datetime.timezone.utc)),
        ),
    ]