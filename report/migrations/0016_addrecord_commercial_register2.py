# Generated by Django 4.1.7 on 2023-06-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0015_alter_addrecord_commercial_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrecord',
            name='commercial_register2',
            field=models.CharField(blank=True, default='1396496', max_length=120, null=True),
        ),
    ]
