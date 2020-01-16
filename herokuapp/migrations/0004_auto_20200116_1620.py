# Generated by Django 2.2.1 on 2020-01-16 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herokuapp', '0003_auto_20200116_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cmnd',
            field=models.IntegerField(default=0, verbose_name='CMND'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Ngày Nhập'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='deposit',
            field=models.CharField(max_length=50, verbose_name='Tiền Đặt Cọc'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='money',
            field=models.CharField(max_length=50, verbose_name='Tiền Còn Thiếu'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='note',
            field=models.TextField(max_length=2000, verbose_name='Ghi Chú'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='number_ticket',
            field=models.CharField(max_length=50, verbose_name='Số Vé Mua'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Số Điện Thoại'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateField(verbose_name='Ngày Đi Tàu'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_time_train',
            field=models.CharField(max_length=50, verbose_name='Giờ Đi'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Trạng Thái'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Tên Khách Hàng'),
        ),
    ]
