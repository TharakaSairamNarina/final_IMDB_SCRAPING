# Generated by Django 3.0.8 on 2020-07-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DATASCRAP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tamil_Movies',
            fields=[
                ('language', models.CharField(max_length=15)),
                ('gener', models.CharField(max_length=15)),
                ('img_url', models.CharField(max_length=500)),
                ('movie', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('rating', models.CharField(max_length=10)),
                ('votes', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=15)),
                ('duration', models.CharField(max_length=10)),
                ('character', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=100)),
                ('introduction', models.CharField(max_length=200)),
            ],
        ),
    ]
