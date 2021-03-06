# Generated by Django 4.0.4 on 2022-05-29 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_comment_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_contract', models.PositiveBigIntegerField()),
                ('desired_reactions', models.PositiveBigIntegerField()),
                ('desired_comments', models.PositiveBigIntegerField()),
                ('threshold_reactions', models.PositiveBigIntegerField()),
                ('threshold_comments', models.PositiveBigIntegerField()),
                ('tips', models.PositiveBigIntegerField()),
                ('total_calculated_price', models.PositiveBigIntegerField()),
                ('until', models.PositiveBigIntegerField()),
                ('status', models.PositiveBigIntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Taken')])),
                ('actualReactions', models.PositiveBigIntegerField()),
                ('actualComments', models.PositiveBigIntegerField()),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisers', to='api.advertiser')),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloggers_contract', to='api.blogger')),
            ],
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
    ]
