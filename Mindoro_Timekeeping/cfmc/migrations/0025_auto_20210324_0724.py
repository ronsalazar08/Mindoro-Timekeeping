# Generated by Django 3.0.7 on 2021-03-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfmc', '0024_auto_20210322_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(upload_to='content_file_name'),
        ),
    ]