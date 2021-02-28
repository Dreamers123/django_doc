# Generated by Django 3.1.5 on 2021-02-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('instructions', models.CharField(blank=True, max_length=4000, null=True)),
                ('region', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField(default='test')),
                ('image_url', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]