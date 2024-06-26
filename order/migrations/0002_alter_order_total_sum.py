# Generated by Django 5.0.6 on 2024-06-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_sum",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
    ]
