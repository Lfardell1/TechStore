# Generated by Django 4.2.4 on 2024-01-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeproduct',
            name='costPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]