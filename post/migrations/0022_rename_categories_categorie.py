# Generated by Django 5.0.4 on 2024-07-11 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_rename_category_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
    ]
