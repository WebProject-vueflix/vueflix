# Generated by Django 3.2.12 on 2022-05-26 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_popularmovie_genre_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingmovie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='upcomingmovie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='upcomingmovie',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='upcomingmovie',
            name='like_users',
        ),
        migrations.DeleteModel(
            name='NowPlayingMovie',
        ),
        migrations.DeleteModel(
            name='UpcomingMovie',
        ),
    ]
