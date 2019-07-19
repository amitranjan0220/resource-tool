from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MyResource(models.Model):
    Unassigned = 'Unassigned'
    Assigned = 'Assigned'
    STATUS = [
    ('Unassigned','Unassigned'),
    ('Assigned','Assigned')
    ]
    rsc_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rsc_name = models.CharField(max_length=100)
    rsc_ip = models.CharField(max_length=20)
    rsc_comment = models.TextField(max_length=50)
    rsc_status = models.CharField(max_length=30,choices=STATUS, default=Unassigned)
   
    def __str__(self):
        return self.rsc_name