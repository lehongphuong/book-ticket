# Generated by Django 2.2.1 on 2020-01-30 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('herokuapp', '0004_auto_20200116_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Ngày Tàu Về'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='end_time_train',
            field=models.TimeField(default=django.utils.timezone.now, max_length=50, verbose_name='Giờ Về'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateField(verbose_name='Ngày Tàu Đi'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_time_train',
            field=models.TimeField(max_length=50, verbose_name='Giờ Đi'),
        ),
    ]
