# Generated by Django 2.0.3 on 2018-04-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_read_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(default=0),
        ),
    ]