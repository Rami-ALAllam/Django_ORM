# Generated by Django 2.2.4 on 2023-11-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_controll_app', '0002_auto_20231126_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
