# Generated by Django 4.0.1 on 2022-01-21 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_strategy_id_photo_strategy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.state'),
        ),
    ] 
