# Generated by Django 3.2 on 2021-06-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreview', '0009_alter_customuser_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
    ]