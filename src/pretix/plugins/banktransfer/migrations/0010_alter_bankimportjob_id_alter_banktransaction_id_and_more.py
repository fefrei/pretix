# Generated by Django 4.1.9 on 2023-07-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banktransfer', '0009_banktransaction_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankimportjob',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='banktransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='refundexport',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
