# Generated by Django 4.1 on 2023-03-09 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0048_stock_item_voucher_voucher_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_transcations',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.voucher'),
        ),
    ]
