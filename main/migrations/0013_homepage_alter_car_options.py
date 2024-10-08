# Generated by Django 5.1 on 2024-09-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_caroption_optioncategory_car_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='homepage_images/')),
                ('image2', models.ImageField(upload_to='homepage_images/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='Options',
            field=models.ManyToManyField(blank=True, null=True, related_name='cars', to='main.caroption'),
        ),
    ]
