# Generated by Django 3.0.7 on 2021-11-24 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20211124_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='transmition',
            new_name='transmission',
        ),
    ]
