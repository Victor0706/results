# Generated by Django 5.0.3 on 2024-08-13 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0002_alter_article_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='upload',
            field=models.FileField(upload_to='photos/%Y/%m/%d'),
        ),
    ]
