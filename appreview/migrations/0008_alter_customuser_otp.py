# Generated by Django 3.2 on 2021-06-18 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreview', '0007_auto_20210617_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
