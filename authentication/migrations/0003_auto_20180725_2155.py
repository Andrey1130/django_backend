# Generated by Django 2.0.2 on 2018-07-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20180725_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='externalURL',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]