# Generated by Django 4.0.2 on 2022-02-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images', verbose_name=''),
        ),
    ]
