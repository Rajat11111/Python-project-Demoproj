# Generated by Django 3.2 on 2021-06-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreview', '0008_alter_customuser_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
