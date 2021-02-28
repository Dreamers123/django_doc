# Generated by Django 3.1.5 on 2021-01-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_runner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Runner',
        ),
    ]
