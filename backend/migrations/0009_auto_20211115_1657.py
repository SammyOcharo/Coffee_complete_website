# Generated by Django 3.2.8 on 2021-11-15 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_customer_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='Images',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Coffee_image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
