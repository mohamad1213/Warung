# Generated by Django 2.2 on 2020-09-10 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateField(default=datetime.datetime.now)),
                ('jumlah', models.IntegerField(default='')),
                ('ket', models.TextField(default='')),
            ],
        ),
    ]
