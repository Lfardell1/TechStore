# Generated by Django 3.2 on 2024-01-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_remove_usermodel_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.TextField(max_length=50),
        ),
    ]