# Generated by Django 4.1 on 2023-03-06 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_bank_transcations_receipt_voucher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit_note',
            name='voucher',
        ),
        migrations.AddField(
            model_name='stock_itemcreation',
            name='godown',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.godown_items'),
        ),
    ]
