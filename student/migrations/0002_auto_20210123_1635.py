# Generated by Django 3.1.5 on 2021-01-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='mob_no',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterModelTable(
            name='students',
            table='student',
        ),
    ]
