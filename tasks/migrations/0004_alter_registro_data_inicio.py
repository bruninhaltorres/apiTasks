# Generated by Django 4.2.7 on 2023-11-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_registro_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='data_inicio',
            field=models.DateField(),
        ),
    ]