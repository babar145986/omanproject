# Generated by Django 4.1.7 on 2023-06-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_addrecord_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrecord',
            name='usage_type',
            field=models.CharField(blank=True, default='استثمار', max_length=120, null=True),
        ),
    ]
