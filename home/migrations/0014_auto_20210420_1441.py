# Generated by Django 3.1.7 on 2021-04-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_transfer_money_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer_money',
            name='Amount',
        ),
        migrations.AddField(
            model_name='transfer_money',
            name='Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
