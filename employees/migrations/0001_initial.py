# Generated by Django 4.1.3 on 2022-11-15 14:28

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('patronymic', models.CharField(max_length=128)),
                ('birthday', models.DateField()),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.position')),
            ],
        ),
    ]
