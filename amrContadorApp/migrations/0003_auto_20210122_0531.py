# Generated by Django 3.1.5 on 2021-01-22 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amrContadorApp', '0002_auto_20210121_1422'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='amrcontador',
            unique_together={('numeroContador',)},
        ),
    ]
