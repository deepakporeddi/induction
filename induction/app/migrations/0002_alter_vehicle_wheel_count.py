# Generated by Django 3.2.16 on 2022-10-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='wheel_count',
            field=models.IntegerField(null=True),
        ),
    ]
