# Generated by Django 4.1.7 on 2023-07-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_alter_personaldetail_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='zone',
            field=models.CharField(blank=True, choices=[('NORTH-EAST', 'North-East'), ('NORTH-WEST', 'North-West'), ('NORTH-CENTRAL', 'North-Central'), ('SOUTH-EAST', 'South-East'), ('SOUTH-WEST', 'South-West'), ('SOUTH-SOUTH', 'South-South')], max_length=300, null=True),
        ),
    ]
