# Generated by Django 2.1.7 on 2019-04-25 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sl10', '0004_auto_20190425_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='description',
            new_name='descrizione',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='category_type',
            new_name='tipo',
        ),
    ]