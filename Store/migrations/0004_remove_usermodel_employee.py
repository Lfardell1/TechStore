# Generated by Django 3.2 on 2024-01-19 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_auto_20240119_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='employee',
        ),
    ]