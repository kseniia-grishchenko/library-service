# Generated by Django 4.2.7 on 2023-11-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_alter_book_authors_alter_book_daily_annual_fee_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="author",
            name="last_name",
        ),
        migrations.AddField(
            model_name="author",
            name="full_name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
