# Generated by Django 4.1 on 2023-03-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0054_alter_stock_itemcreation_per_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_itemcreation',
            name='per',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stock_itemcreation',
            name='quantity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stock_itemcreation',
            name='rate',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stock_itemcreation',
            name='value',
            field=models.CharField(max_length=100, null=True),
        ),
    ]