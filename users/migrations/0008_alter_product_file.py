# Generated by Django 3.2.9 on 2021-11-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20211119_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, upload_to='users/static/users/downloads/'),
        ),
    ]
