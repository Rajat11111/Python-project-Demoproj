# Generated by Django 3.2 on 2021-06-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreview', '0006_auto_20210617_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
