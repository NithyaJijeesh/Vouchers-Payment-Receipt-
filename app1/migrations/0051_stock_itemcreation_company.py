# Generated by Django 4.1 on 2023-03-17 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0050_alter_stock_item_voucher_per'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_itemcreation',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
