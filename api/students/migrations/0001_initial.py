# Generated by Django 5.1.5 on 2025-01-23 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('districts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(default=None, max_length=50, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='districts.district')),
            ],
        ),
    ]
