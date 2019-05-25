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

    def __str__(self):
        return self.code + " " + self.name

    class Meta:
        """
        Some information about Student class.
        """
        verbose_name = ("Student")
        verbose_name_plural = ("Students")


class Professor(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        ('Name'),
        help_text=("Professor Name"),
        max_length=100,
    )

    email = models.CharField(
        ('Email'),
        help_text=("Professor email"),
        max_length=100,
    )

    class Meta:
        verbose_name = ("Professor")
        verbose_name_plural = ("Professors")

    def __str__(self):
        return self.name
