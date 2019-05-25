from django.db import models

class Student(models.Model):

    code = models.CharField(
        ('Code'),
        help_text=("Student Code"),
        max_length=15,
        primary_key=True
    )

    name = models.CharField(
        ('Name'),
        help_text=("Student Name"),
        max_length=100,
    )

    ira = models.FloatField(
        ('IRA'),
    )

    grade = models.FloatField(
        ('Grade'),
    )

    mention = models.CharField(
        ('Mention'),
        help_text=("Student Mention in the subject"),
        max_length=2,
    )
