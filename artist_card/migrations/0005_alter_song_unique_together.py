# Generated by Django 4.1.7 on 2023-03-08 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist_card', '0004_song_key_alter_song_duration'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('album', 'key')},
        ),
    ]