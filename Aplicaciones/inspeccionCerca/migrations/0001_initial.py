# Generated by Django 5.2.1 on 2025-06-12 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zonaSeguridad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inspeccionCerca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inspector', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('estado', models.CharField()),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zonaSeguridad.zonaseguridad')),
            ],
        ),
    ]
