# Generated by Django 3.2 on 2021-04-14 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('witcher', '0002_auto_20210414_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='name',
        ),
    ]
