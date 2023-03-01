# Generated by Django 4.1.6 on 2023-02-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_account_cash_remove_account_stock_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
        migrations.AddField(
            model_name='account',
            name='stock',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='stock_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
