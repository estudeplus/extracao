# Generated by Django 2.2.1 on 2019-06-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_student_student_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_code',
            field=models.CharField(help_text='Student Code', max_length=255, null=True, verbose_name='Code'),
        ),
    ]
