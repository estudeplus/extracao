from django.db import models
from django.core.validators import FileExtensionValidator


class Document(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    document = models.FileField(
        upload_to='documents/%Y/%m/',
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'csv'])]
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return "Document " + self.id
    
    class Meta:
        """
        Some information about Document class.
        """
        verbose_name = ("Document")
        verbose_name_plural = ("Documents")
