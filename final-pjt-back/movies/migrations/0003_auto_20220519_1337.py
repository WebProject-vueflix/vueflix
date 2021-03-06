# Generated by Django 3.2.12 on 2022-05-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_actor_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowplayingmovie',
            name='actors',
            field=models.ManyToManyField(related_name='nowplaying_movies', to='movies.Actor'),
        ),
        migrations.AlterField(
            model_name='nowplayingmovie',
            name='director',
            field=models.ManyToManyField(related_name='nowplaying_movies', to='movies.Director'),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='actors',
            field=models.ManyToManyField(related_name='popular_movies', to='movies.Actor'),
        ),
        migrations.AlterField(
            model_name='popularmovie',
            name='director',
            field=models.ManyToManyField(related_name='popular_movies', to='movies.Director'),
        ),
        migrations.AlterField(
            model_name='upcomingmovie',
            name='actors',
            field=models.ManyToManyField(related_name='upcoming_movies', to='movies.Actor'),
        ),
        migrations.AlterField(
            model_name='upcomingmovie',
            name='director',
            field=models.ManyToManyField(related_name='upcoming_movies', to='movies.Director'),
        ),
    ]
