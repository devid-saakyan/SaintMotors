# Generated by Django 5.1 on 2024-08-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_tyrebrand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsubmission',
            name='MakeName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carsubmission',
            name='ModelName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
