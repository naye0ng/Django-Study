# Generated by Django 2.1.7 on 2019-03-14 05:50

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='postings/resize/%y/%m/%d'),
        ),
    ]
