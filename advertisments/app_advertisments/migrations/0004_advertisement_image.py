# Generated by Django 4.2.3 on 2023-08-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisments', '0003_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advertisments', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
