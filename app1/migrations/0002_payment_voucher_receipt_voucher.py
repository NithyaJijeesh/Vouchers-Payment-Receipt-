# Generated by Django 4.1 on 2022-12-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(null=True)),
                ('account', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(null=True)),
                ('particulars', models.CharField(max_length=255, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('narration', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='receipt_voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.IntegerField(null=True)),
                ('account', models.CharField(max_length=255, null=True)),
                ('date', models.DateField(null=True)),
                ('particulars', models.CharField(max_length=255, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('narration', models.CharField(max_length=255)),
            ],
        ),
    ]
