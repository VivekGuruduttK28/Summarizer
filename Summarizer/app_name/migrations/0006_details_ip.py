# Generated by Django 4.0.1 on 2023-08-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0005_alter_image_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='ip',
            field=models.GenericIPAddressField(default=0),
            preserve_default=False,
        ),
    ]