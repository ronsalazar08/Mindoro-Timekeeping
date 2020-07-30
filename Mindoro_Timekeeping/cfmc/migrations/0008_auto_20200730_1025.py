# Generated by Django 3.0.8 on 2020-07-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfmc', '0007_auto_20200730_1022'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.UniqueConstraint(fields=('t1', 't2', 't3', 't4', 't5'), name='name of constraint'),
        ),
    ]
