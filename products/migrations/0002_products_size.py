# Generated by Django 4.2.4 on 2023-08-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=50, null=True),
        ),
    ]
