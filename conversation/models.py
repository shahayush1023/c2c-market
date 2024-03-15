from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.

class Conversation(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='conversations')
    members = models.ManyToManyField(User,related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
      ordering = ('-modified_at',)
      
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE,related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)
    
    

