# Generated by Django 4.1.9 on 2023-07-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal', '0003_migrate_to_v2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencedpaypalobject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
