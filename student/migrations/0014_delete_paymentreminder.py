# Generated by Django 4.2.6 on 2023-10-22 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_feesmaster_fined'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentReminder',
        ),
    ]
