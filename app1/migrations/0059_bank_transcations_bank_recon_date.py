# Generated by Django 4.1 on 2023-03-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0058_payment_particulars_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_transcations',
            name='bank_recon_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]