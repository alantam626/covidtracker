# Generated by Django 4.0.1 on 2022-01-21 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_vaccine_card_photo_strategy_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='strategy_id',
            new_name='strategy',
        ),
    ]