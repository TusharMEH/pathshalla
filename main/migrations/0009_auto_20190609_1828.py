# Generated by Django 2.1 on 2019-06-09 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190609_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_category',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series'),
        ),
    ]
