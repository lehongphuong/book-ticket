from django.db import models
import datetime

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# https://docs.djangoproject.com/en/2.2/topics/db/sql/


class Customer(models.Model):
    id = models.AutoField
    cmnd = models.IntegerField('CMND', default=0)
    username = models.CharField('Tên Khách Hàng', max_length=50)
    phone = models.CharField('Số Điện Thoại', max_length=30)
    number_ticket = models.CharField('Số Vé Mua', max_length=50)
    deposit = models.CharField('Tiền Đặt Cọc', max_length=50)
    money = models.CharField('Tiền Còn Thiếu', max_length=50)
    create_date = models.DateField('Ngày Nhập', default=datetime.date.today)
    start_date = models.DateField('Ngày Đi Tàu')
    start_time_train = models.CharField('Giờ Đi', max_length=50)
    note = models.TextField('Ghi Chú', max_length=2000)
    status = models.IntegerField('Trạng Thái', default=0)
