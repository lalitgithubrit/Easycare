# Generated by Django 4.2.6 on 2024-04-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medisafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ambulance_No', models.IntegerField()),
                ('Family_No', models.IntegerField()),
            ],
        ),
    ]