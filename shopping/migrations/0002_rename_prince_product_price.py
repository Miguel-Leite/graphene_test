# Generated by Django 3.2.3 on 2021-08-18 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prince',
            new_name='price',
        ),
    ]
