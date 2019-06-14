# Generated by Django 2.2.1 on 2019-05-29 02:32

from django.db import migrations, models
import extracao.core.states


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_document_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='extension',
            field=models.CharField(choices=[(extracao.core.states.Extensions('xlsx'), 'xlsx'), (extracao.core.states.Extensions('csv'), 'csv')], default=None, max_length=10, null=True),
        ),
    ]
