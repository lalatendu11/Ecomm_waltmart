# Generated by Django 5.0.1 on 2024-01-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('mob', models.IntegerField(primary_key=True, serialize=False)),
                ('gmail', models.EmailField(max_length=254)),
                ('house_no', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
            ],
        ),
    ]
