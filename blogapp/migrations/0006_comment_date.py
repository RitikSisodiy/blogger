# Generated by Django 3.1.5 on 2021-01-30 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
