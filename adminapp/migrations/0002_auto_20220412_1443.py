# Generated by Django 3.2.12 on 2022-04-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("adminapp", "0001_initial")]

    operations = [
        migrations.DeleteModel(name="Contact"),
        migrations.DeleteModel(name="Product"),
        migrations.DeleteModel(name="ProductCategory"),
    ]
