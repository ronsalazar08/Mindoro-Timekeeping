# Generated by Django 3.0.8 on 2020-07-30 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfmc', '0016_auto_20200730_1111'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('t2', 't3', 't4', 't5')},
        ),
    ]
