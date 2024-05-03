# Generated by Django 5.0.4 on 2024-05-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='largeContent',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='teacherStutus',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]