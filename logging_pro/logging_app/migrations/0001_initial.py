# Generated by Django 5.0 on 2023-12-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('roll_no', models.IntegerField()),
                ('dob', models.DateField()),
                ('marks', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
