# Generated by Django 2.2.4 on 2019-09-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
