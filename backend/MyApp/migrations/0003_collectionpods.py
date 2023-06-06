# Generated by Django 4.2.1 on 2023-06-05 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_creator_remove_playlist_user_remove_track_playlist_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_casts', models.CharField(max_length=100)),
                ('cast_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.podcasts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.user')),
            ],
        ),
    ]
