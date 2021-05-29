# Generated by Django 3.0.14 on 2021-05-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_body2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='visits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
