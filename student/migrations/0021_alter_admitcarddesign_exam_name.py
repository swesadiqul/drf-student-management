# Generated by Django 4.2.6 on 2023-10-23 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_alter_examgroup_no_of_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admitcarddesign',
            name='exam_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.exam'),
        ),
    ]
