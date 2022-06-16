from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=False)
    User = get_user_model()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
            return self.title, self.author
                
