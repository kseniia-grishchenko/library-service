# Generated by Django 4.2.7 on 2023-11-26 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("borrowings", "0008_alter_borrowing_expected_return_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="expected_return_date",
            field=models.DateTimeField(default=datetime.date(2023, 12, 17), null=True),
        ),
    ]
