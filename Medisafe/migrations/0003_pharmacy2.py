# Generated by Django 4.2.6 on 2024-04-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medisafe', '0002_emergency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diseases2', models.CharField(max_length=50)),
                ('Medicine2', models.CharField(max_length=50)),
            ],
        ),
    ]