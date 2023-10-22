# Generated by Django 4.2.6 on 2023-10-22 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_delete_paymentreminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fees_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='student.feesmaster'),
        ),
        migrations.AlterField(
            model_name='student',
            name='fees_payments',
            field=models.ManyToManyField(blank=True, related_name='student_payments', to='student.payment'),
        ),
    ]
