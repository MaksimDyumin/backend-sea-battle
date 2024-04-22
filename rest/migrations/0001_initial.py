# Generated by Django 5.0.4 on 2024-04-22 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isShip', models.BooleanField()),
                ('isShooted', models.BooleanField()),
                ('coordinateY', models.IntegerField()),
                ('coordinateX', models.IntegerField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cell', to='rest.board')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='board', to='rest.user'),
        ),
    ]