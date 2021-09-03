# Generated by Django 3.2.6 on 2021-09-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawlers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Category Name')),
                ('url', models.URLField(max_length=100, verbose_name='Category Link')),
                ('new', models.CharField(max_length=10, verbose_name='Is It New?')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'db_table': 'brands',
            },
        ),
    ]
