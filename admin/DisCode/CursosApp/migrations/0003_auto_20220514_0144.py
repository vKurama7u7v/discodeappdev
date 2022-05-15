# Generated by Django 3.0.5 on 2022-05-14 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CursosApp', '0002_codigo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codigo',
            options={'verbose_name': 'codigo', 'verbose_name_plural': 'codigos'},
        ),
        migrations.AddField(
            model_name='codigo',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]
