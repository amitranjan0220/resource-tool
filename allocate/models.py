from django.db import models
from django.contrib.auth.models import User
from my_resource.models import Category, MyResource
# Create your models here.

class AllocateResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(MyResource, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100,default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ["-created_at"]

class SearchByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SearchByResource(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    resource = models.ForeignKey(MyResource, on_delete=models.CASCADE)
