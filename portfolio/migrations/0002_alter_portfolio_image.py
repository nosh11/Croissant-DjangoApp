# Generated by Django 5.1.6 on 2025-02-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/images/'),
        ),
    ]
