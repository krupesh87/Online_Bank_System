# Generated by Django 3.1.7 on 2021-04-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210420_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer_money',
            name='Amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
