# Generated by Django 2.2.4 on 2023-11-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_controll_app', '0003_auto_20231126_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='desc',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
