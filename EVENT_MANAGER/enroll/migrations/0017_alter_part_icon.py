# Generated by Django 4.0.1 on 2022-01-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0016_alter_part_rno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='icon',
            field=models.PositiveBigIntegerField(max_length=256),
        ),
    ]
