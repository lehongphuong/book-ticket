# Generated by Django 2.2.1 on 2020-01-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herokuapp', '0003_auto_20200113_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]
