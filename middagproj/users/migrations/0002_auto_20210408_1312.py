# Generated by Django 3.1.6 on 2021-04-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='allergy',
            constraint=models.UniqueConstraint(fields=('allergy',), name='unique_allergy'),
        ),
    ]
