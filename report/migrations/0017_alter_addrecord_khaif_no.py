# Generated by Django 4.1.7 on 2023-06-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0016_addrecord_commercial_register2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrecord',
            name='khaif_no',
            field=models.CharField(blank=True, default='0000000', max_length=120, null=True),
        ),
    ]