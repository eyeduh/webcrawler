# Generated by Django 3.2.6 on 2021-09-04 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawlers', '0013_auto_20210904_1005'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]
