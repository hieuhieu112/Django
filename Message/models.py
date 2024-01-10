from django.db import models
from django.utils import timezone
from User.models import User
from Group.models import Group
# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, null=False, on_delete= models.CASCADE, related_name='sender')
    time_send = models.DateTimeField(auto_now_add=True, null=False)
    type = models.IntegerField(default=0)# message, call, notify
    message = models.CharField(max_length=1000, blank=False,null=False)
    to_group = models.ForeignKey(Group, blank=True,null=True, on_delete= models.CASCADE)# default la gui nguoi nhan
    receiver = models.ForeignKey(User, null=True, on_delete= models.CASCADE, related_name='receiver')
    status = models.BooleanField(default=True)  # False la da duoc go

    class Meta:
        ordering = ('time_send',)
