# Generated by Django 4.1.7 on 2023-07-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_alter_governmentappointment_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='governmentappointment',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
