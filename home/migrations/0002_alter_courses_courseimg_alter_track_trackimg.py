# Generated by Django 4.0.6 on 2022-10-04 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='courseImg',
            field=models.ImageField(upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='track',
            name='TrackImg',
            field=models.ImageField(upload_to='photo'),
        ),
    ]
