# Generated by Django 3.2.16 on 2022-10-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_vehicle_wheel_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
