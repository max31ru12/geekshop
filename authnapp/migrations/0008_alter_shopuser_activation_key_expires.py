# Generated by Django 3.2.12 on 2022-05-02 21:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0007_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 21, 47, 29, 703177, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
