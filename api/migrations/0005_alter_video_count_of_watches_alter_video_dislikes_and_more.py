# Generated by Django 4.0.4 on 2022-05-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_platformaction_tx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='count_of_watches',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='medium_time_watching',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
