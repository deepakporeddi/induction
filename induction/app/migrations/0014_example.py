# Generated by Django 3.2.16 on 2022-10-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20221026_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
            ],
        ),
    ]