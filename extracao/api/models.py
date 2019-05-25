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
        help_text=("Student academic performance Index"),
    )

    grade = models.FloatField(
        ('Grade'),
        help_text=("Student grade on the tutor selection process"),
    )

    mention = models.CharField(
        ('Mention'),
        help_text=("Student Mention in the subject"),
        max_length=2,
    )
