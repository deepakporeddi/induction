# Generated by Django 3.2.16 on 2022-10-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
