# Generated by Django 4.0.1 on 2022-01-27 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_market_options_alter_strategy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='market',
            options={'verbose_name': 'MARKET', 'verbose_name_plural': 'MARKETS'},
        ),
    ]
