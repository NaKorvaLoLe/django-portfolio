# Generated by Django 4.1.5 on 2023-11-12 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descroption',
            new_name='description',
        ),
    ]
