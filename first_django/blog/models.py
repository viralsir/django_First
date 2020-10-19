from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    author=models.CharField(max_length=30)

    def __str__(self):
        return f"Post(title={self.title},author={self.author})"


