# Generated by Django 2.0.13 on 2019-07-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190703_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sports'),
        ),
        migrations.AlterField(
            model_name='post',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sportart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
