# Generated by Django 4.2.2 on 2023-07-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]
