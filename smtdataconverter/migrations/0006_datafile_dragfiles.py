# Generated by Django 2.2.1 on 2019-08-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smtdataconverter', '0005_remove_datafile_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='dragfiles',
            field=models.TextField(blank=True, verbose_name='file text'),
        ),
    ]