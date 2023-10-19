# Generated by Django 4.2.6 on 2023-10-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_remove_feescollect_payment_feescollect_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feescollect',
            name='payment',
        ),
        migrations.AddField(
            model_name='feescollect',
            name='payment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.payment'),
        ),
    ]
