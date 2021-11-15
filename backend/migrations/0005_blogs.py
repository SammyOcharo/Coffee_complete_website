# Generated by Django 3.2.8 on 2021-11-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20211102_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_created=True)),
                ('Images', models.ImageField(upload_to='static/images')),
                ('Title', models.CharField(max_length=50)),
                ('Writer', models.CharField(max_length=50)),
                ('Details', models.TextField()),
            ],
        ),
    ]
