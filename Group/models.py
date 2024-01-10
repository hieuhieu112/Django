from django.db import models
from django.utils import timezone
from User.models import User
# Create your models here.



class Group(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timeCreate = models.DateTimeField(auto_now_add=True, null = False)
    name = models.CharField(max_length=200, null= False)
    status = models.BooleanField(default=True)# False la khong hoat ong


class DetailGroup(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=False, on_delete= models.CASCADE)
    timeJoin = models.DateTimeField(auto_now_add=True, null = False)
    role = models.IntegerField(default=0)# truong nhom, pho nhom, thanh vien
    status = models.BooleanField(default=True)  # False la roi nhom roi
