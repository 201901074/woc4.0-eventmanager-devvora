# Generated by Django 4.0.1 on 2022-01-31 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0020_alter_part_iemail_alter_reg_hemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='iemail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='reg',
            name='hemail',
            field=models.EmailField(max_length=254),
        ),
    ]