# Generated by Django 5.1 on 2024-08-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_plates'),
    ]

    operations = [
        migrations.AddField(
            model_name='plates',
            name='Price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
