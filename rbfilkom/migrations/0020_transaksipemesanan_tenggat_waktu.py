# Generated by Django 2.1b1 on 2019-02-18 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbfilkom', '0019_transaksipemesanan_antrian'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksipemesanan',
            name='tenggat_waktu',
            field=models.DateField(default=datetime.datetime(2019, 2, 18, 14, 33, 25, 152501)),
        ),
    ]
