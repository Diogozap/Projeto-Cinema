# Generated by Django 5.1.1 on 2024-10-04 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='ano',
            field=models.DateField(),
        ),
    ]
