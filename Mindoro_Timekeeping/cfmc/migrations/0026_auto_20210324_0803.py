# Generated by Django 3.0.7 on 2021-03-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfmc', '0025_auto_20210324_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='picture',
        ),
        migrations.AddField(
            model_name='employee',
            name='picture1',
            field=models.ImageField(default='', upload_to='content_file_name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='picture2',
            field=models.ImageField(default='', upload_to='content_file_name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='picture3',
            field=models.ImageField(default='', upload_to='content_file_name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='picture4',
            field=models.ImageField(default='', upload_to='content_file_name'),
        ),
        migrations.AddField(
            model_name='employee',
            name='picture5',
            field=models.ImageField(default='', upload_to='content_file_name'),
        ),
    ]