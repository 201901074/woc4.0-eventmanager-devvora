# Generated by Django 4.0.1 on 2022-01-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0012_alter_part_rnog_alter_part_rnoi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='rnog',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='rnoi',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
