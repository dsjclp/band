# Generated by Django 3.0.6 on 2020-06-05 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200604_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='image4',
        ),
    ]