# Generated by Django 5.0.1 on 2024-02-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0002_lawyer_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]