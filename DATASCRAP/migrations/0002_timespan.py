# Generated by Django 3.0.8 on 2020-07-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DATASCRAP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSpan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Telugu_update_time', models.TimeField()),
            ],
        ),
    ]
