from django.db import models
import uuid 

class UserReg(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    phone_number = models.CharField(max_length=200)
    jam = models.CharField(max_length=100)
    names = models.JSONField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

    




