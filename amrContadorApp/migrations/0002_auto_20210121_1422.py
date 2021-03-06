# Generated by Django 3.1.5 on 2021-01-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amrContadorApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='faceACurr',
            field=models.FloatField(blank=True, null=True, verbose_name='Face A de corriente (A)'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='faceBCurr',
            field=models.FloatField(blank=True, null=True, verbose_name='Face B de corriente (A)'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='faceCCurr',
            field=models.FloatField(blank=True, null=True, verbose_name='Face C de corriente (A)'),
        ),
    ]
