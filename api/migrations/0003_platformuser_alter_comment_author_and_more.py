# Generated by Django 4.0.4 on 2022-05-28 15:12

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_video_content_file_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('reactions', models.PositiveIntegerField(default=0)),
                ('comments', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_video', to='api.video'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='advertiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisers', to='api.advertiser'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='blogger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloggers_contract', to='api.blogger'),
        ),
        migrations.AlterField(
            model_name='video',
            name='blogger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloggers_video', to='api.blogger'),
        ),
        migrations.AlterField(
            model_name='video',
            name='content_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='./static/videos/'), upload_to=''),
        ),
        migrations.CreateModel(
            name='PlatformAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(max_length=100)),
                ('tx', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.platformuser')),
            ],
        ),
    ]