# Generated by Django 2.2.1 on 2019-06-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=None, help_text='Student Email', max_length=100, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
