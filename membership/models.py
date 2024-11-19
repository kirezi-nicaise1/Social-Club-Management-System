from django.db import models

from django.db import models

class Member(models.Model):
    member_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    membership_type = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

