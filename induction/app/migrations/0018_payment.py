# Generated by Django 3.2.16 on 2022-10-27 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_club_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(max_length=35)),
                ('paid_to', models.CharField(max_length=40)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
