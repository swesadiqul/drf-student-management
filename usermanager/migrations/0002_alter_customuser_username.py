# Generated by Django 4.2.6 on 2023-10-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True),
        ),
    ]
