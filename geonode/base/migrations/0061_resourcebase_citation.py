# Generated by Django 2.2.28 on 2022-10-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0060_auto_20210512_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='citation',
            field=models.TextField(blank=True, help_text='publications', max_length=500, null=True, verbose_name='citation'),
        ),
    ]
