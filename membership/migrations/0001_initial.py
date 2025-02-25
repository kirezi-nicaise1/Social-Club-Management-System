# Generated by Django 5.1.2 on 2024-11-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('membership_type', models.CharField(max_length=50)),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
