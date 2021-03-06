# Generated by Django 2.2.1 on 2019-06-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190616_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.CharField(help_text='Professor email', max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(help_text='Professor Name', max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(help_text='Student Email', max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.FloatField(help_text='Student grade on the tutor selection process', null=True, verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='ira',
            field=models.FloatField(help_text='Student academic performance Index', null=True, verbose_name='IRA'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mention',
            field=models.CharField(help_text='Student Mention in the subject', max_length=255, null=True, verbose_name='Mention'),
        ),
    ]
