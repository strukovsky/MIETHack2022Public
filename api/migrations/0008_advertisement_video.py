# Generated by Django 4.0.4 on 2022-05-29 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_advertisement_delete_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='api.video'),
        ),
    ]
