# Generated by Django 4.0.1 on 2022-01-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0008_part_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='eid',
            field=models.CharField(max_length=256),
        ),
    ]
