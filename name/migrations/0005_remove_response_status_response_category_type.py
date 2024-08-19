# Generated by Django 5.0.3 on 2024-08-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0004_rename_authoruser_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='status',
        ),
        migrations.AddField(
            model_name='response',
            name='category_type',
            field=models.CharField(choices=[('CN', 'Рассмотрение'), ('AC', 'Принято'), ('RM', 'Удалено')], default='CN', max_length=2),
        ),
    ]
