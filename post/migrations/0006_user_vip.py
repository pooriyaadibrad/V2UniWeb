# Generated by Django 5.0.4 on 2024-05-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vip',
            field=models.BooleanField(default=False),
        ),
    ]