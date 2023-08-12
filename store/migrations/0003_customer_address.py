# Generated by Django 4.2.4 on 2023-08-12 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=100)),
                ('tole_name', models.CharField(max_length=100)),
                ('customerid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
    ]
