# Generated by Django 2.1.8 on 2019-04-12 14:09

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(upload_to='boards/images'),
        ),
    ]
