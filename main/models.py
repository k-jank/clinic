from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('dokter', 'Dokter'),
        ('pasien', 'Pasien'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    full_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    contact = models.CharField(max_length=15, blank=True)

    def is_admin(self):
        return self.role == 'admin'

    def is_dokter(self):
        return self.role == 'dokter'

    def is_pasien(self):
        return self.role == 'pasien'
