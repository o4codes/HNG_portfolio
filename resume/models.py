from django.db import models

# Create your models here

class contact(models.Model):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    message = models.TextField(blank=False, null = False)
    date_time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email