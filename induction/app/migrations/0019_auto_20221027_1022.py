# Generated by Django 3.2.16 on 2022-10-27 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payer',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='paid_to',
        ),
    ]
