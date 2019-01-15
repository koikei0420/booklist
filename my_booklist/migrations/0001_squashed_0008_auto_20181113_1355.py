# Generated by Django 2.1.1 on 2018-11-20 12:18

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('my_booklist', '0001_initial'), ('my_booklist', '0002_auto_20181022_0536'), ('my_booklist', '0003_auto_20181022_1514'), ('my_booklist', '0004_auto_20181022_1519'), ('my_booklist', '0005_book_isbn'), ('my_booklist', '0006_auto_20181112_1939'), ('my_booklist', '0007_auto_20181112_2103'), ('my_booklist', '0008_auto_20181113_1355')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author1', models.CharField(max_length=50)),
                ('author2', models.CharField(blank=True, max_length=50, null=True)),
                ('author3', models.CharField(blank=True, max_length=50, null=True)),
                ('author4', models.CharField(blank=True, max_length=200, null=True)),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('qm', '量子力学(qm)'), ('qo', '量子光学(qo)'), ('qi', '量子情報(qi)'), ('qp', '量子物理学(qp)'), ('qf', '場の量子論(qf)'), ('ss', '固体物理学・超伝導(ss)'), ('sm', '統計力学(sm)'), ('em', '電磁気学(em)'), ('am', '力学・解析力学(am)'), ('ph', '物理学一般(ph)'), ('pp', '確率過程(pp)'), ('nc', '計算機・数値計算(nc)'), ('mt', '数学(mt)'), ('ot', 'その他(ot)')], max_length=2)),
                ('rent_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('rent_flag', models.BooleanField(default=False)),
                ('rent_user', models.CharField(blank=True, max_length=50, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]+$'), django.core.validators.MinLengthValidator(10)])),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]