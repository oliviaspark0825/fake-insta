# Generated by Django 2.1.8 on 2019-04-12 14:09

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190412_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(upload_to='posts/images'),
        ),
    ]
