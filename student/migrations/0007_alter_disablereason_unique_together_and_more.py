# Generated by Django 4.2.6 on 2023-10-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_disablereason_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='disablereason',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='disablereason',
            name='disable_name',
            field=models.CharField(max_length=50),
        ),
    ]
