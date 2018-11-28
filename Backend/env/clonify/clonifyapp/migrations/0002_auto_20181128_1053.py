# Generated by Django 2.1.3 on 2018-11-28 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clonifyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clonifyapp.Song')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='songplaylist',
            name='playlist',
        ),
        migrations.RemoveField(
            model_name='songplaylist',
            name='song',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='name',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.AddField(
            model_name='playlist',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clonifyapp.Song'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SongPlaylist',
        ),
        migrations.AddField(
            model_name='playlist',
            name='playlist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clonifyapp.Playlists'),
            preserve_default=False,
        ),
    ]