# Generated by Django 4.1.7 on 2023-06-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_addrecord_raqmul_qareebi'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrecord',
            name='raqmul_qatga',
            field=models.CharField(blank=True, default='125', max_length=120, null=True),
        ),
    ]
