# Generated by Django 3.2 on 2021-06-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreview', '0011_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
