# Generated by Django 3.0.5 on 2020-05-04 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200503_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.IntegerField(max_length=32, verbose_name='Edition'),
        ),
    ]
