# Generated by Django 3.0.4 on 2020-03-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_remove_garbage_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garbage',
            name='image',
            field=models.ImageField(upload_to='garbage_product/'),
        ),
    ]
