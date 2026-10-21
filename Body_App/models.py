from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator
)


class Student(models.Model):
    COURSE_CHOICES = [
        ('BSCS', 'BS Computer Science'),
        ('BSIT', 'BS Information Technology'),
        ('BSIS', 'BS Information Systems'),
    ]

    name      = models.CharField(max_length=100)
    email     = models.EmailField(unique=True)
    age       = models.IntegerField(
                    validators=[
                        MinValueValidator(15),
                        MaxValueValidator(60),
                    ]
                )
    course    = models.CharField(
                    max_length=10,
                    choices=COURSE_CHOICES,
                    default='BSCS'
                )
    gpa       = models.DecimalField(
                    max_digits=3,
                    decimal_places=2,
                    default=0.00
                )
    is_active = models.BooleanField(default=True)
    bio       = models.TextField(blank=True, null=True)
    enrolled  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
