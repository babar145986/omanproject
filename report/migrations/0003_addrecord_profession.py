# Generated by Django 4.1.7 on 2023-06-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_alter_addrecord_contract_fees_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrecord',
            name='profession',
            field=models.CharField(blank=True, default=' إصلاح ميكانيك المركبات', max_length=120, null=True),
        ),
    ]