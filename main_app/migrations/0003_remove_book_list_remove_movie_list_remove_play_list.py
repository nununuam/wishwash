# Generated by Django 4.0.4 on 2022-05-07 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_movie_book_remove_movie_plays_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='list',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='list',
        ),
        migrations.RemoveField(
            model_name='play',
            name='list',
        ),
    ]