# Generated by Django 3.1.7 on 2021-04-20 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210420_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer_money',
            name='Amount',
        ),
    ]