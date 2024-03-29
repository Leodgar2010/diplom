# Generated by Django 5.0.1 on 2024-01-29 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelapp.person')),
                ('client_account', models.DecimalField(decimal_places=2, max_digits=13)),
            ],
            bases=('modelapp.person',),
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelapp.person')),
                ('lawyer_accesibility', models.BooleanField(default=True)),
                ('lawyer_photo', models.ImageField(upload_to='lawyer_photo/')),
            ],
            bases=('modelapp.person',),
        ),
    ]
