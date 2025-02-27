# Generated by Django 5.1.5 on 2025-02-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_rename_country_shippingaddress_shipping_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_phone_number',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_state',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_zipcode',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
