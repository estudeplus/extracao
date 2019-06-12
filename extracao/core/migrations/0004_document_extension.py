# Generated by Django 2.2.1 on 2019-05-29 02:16

from django.db import migrations, models
import extracao.core.states


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190526_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='extension',
            field=models.CharField(choices=[(extracao.core.states.Extensions('xlsx'), 'xlsx'), (extracao.core.states.Extensions('csv'), 'csv')], default=None, max_length=4, null=True),
        ),
    ]