# Generated by Django 3.1.7 on 2021-04-17 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210417_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer_money',
            old_name='RecieverName',
            new_name='ReceiverName',
        ),
    ]
