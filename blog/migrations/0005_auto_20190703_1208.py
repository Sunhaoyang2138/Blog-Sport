# Generated by Django 2.0.13 on 2019-07-03 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190703_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sport',
            new_name='sportart',
        ),
    ]