# Generated by Django 3.1.5 on 2021-01-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('medal', models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10)),
            ],
        ),
    ]