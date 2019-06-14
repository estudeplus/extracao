from django.db import models


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


class Subject(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    code = models.CharField(
        ('Code'),
        help_text=("Subject Code"),
        max_length=15,
    )

    name = models.CharField(
        ('Name'),
        help_text=("Subject Name"),
        max_length=50,
    )

    class_code = models.CharField(
        ('Class Code'),
        help_text=("Class Code"),
        max_length=10,
    )

    professor = models.ForeignKey(
        Professor,
        related_name="subjects",
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = ("Subject")
        verbose_name_plural = ("Subjects")

    def __str__(self):
        return self.name


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

    email = models.CharField(
        ('Email'),
        help_text=("Student Email"),
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

    subject = models.ForeignKey(
        Subject,
        related_name="tutors",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.code + " " + self.name

    class Meta:
        """
        Some information about Student class.
        """
        verbose_name = ("Student")
        verbose_name_plural = ("Students")