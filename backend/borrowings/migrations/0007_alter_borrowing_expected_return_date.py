# Generated by Django 4.2.7 on 2023-11-26 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("borrowings", "0006_alter_borrowing_expected_return_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="expected_return_date",
            field=models.DateField(
                default=datetime.datetime(2023, 12, 17, 21, 26, 43, 678134), null=True
            ),
        ),
    ]
