# Generated by Django 3.0.7 on 2021-11-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='passangers',
            field=models.IntegerField(),
        ),
    ]
