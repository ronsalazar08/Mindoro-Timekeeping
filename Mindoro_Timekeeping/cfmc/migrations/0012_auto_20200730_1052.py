# Generated by Django 3.0.8 on 2020-07-30 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfmc', '0011_auto_20200730_1047'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='employee',
            name='name of constraint',
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('t1', 't2', 't3', 't4', 't5')},
        ),
    ]
