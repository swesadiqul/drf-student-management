# Generated by Django 4.2.6 on 2023-10-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0003_remove_customuser_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
