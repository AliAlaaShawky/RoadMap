# Generated by Django 4.0.6 on 2022-10-08 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0005_alter_coursecv_options_alter_trackcv_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecv',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='trackcv',
            options={'ordering': ['-id']},
        ),
    ]
