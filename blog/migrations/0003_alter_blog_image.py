# Generated by Django 4.1.5 on 2023-11-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/images'),
        ),
    ]
