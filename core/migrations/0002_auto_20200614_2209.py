# Generated by Django 2.2.13 on 2020-06-14 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='publish_date',
            new_name='published',
        ),
    ]
