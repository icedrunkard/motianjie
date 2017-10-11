# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school',
            field=models.CharField(choices=[('BIT', '北京理工大学'), ('THU', '清华大学'), ('XMU', '厦门大学'), ('SJTU', '上海交通大学'), ('PKU', '北京大学'), ('BNU', '北京师范大学'), ('TONGJI', '同济大学'), ('RENMIN', '中国人民大学'), ('FUDAN', '复旦大学'), ('ZJU', '浙江大学'), ('BUAA', '北京航空航天大学')], default=None, max_length=300),
        ),
    ]