# Generated by Django 2.1 on 2019-06-09 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_category',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
    ]