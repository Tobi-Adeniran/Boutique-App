# Generated by Django 3.2.13 on 2022-09-10 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='email',
        ),
    ]