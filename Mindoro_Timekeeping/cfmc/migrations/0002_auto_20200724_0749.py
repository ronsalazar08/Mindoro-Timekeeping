# Generated by Django 3.0.8 on 2020-07-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfmc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='t2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='t3',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='t4',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='t5',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(blank=True, choices=[('P', 'Present'), ('L', 'Late'), ('A', 'Absent')], max_length=5),
        ),
    ]
