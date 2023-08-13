from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    image = models.ImageField(upload_to='./image/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    summury = models.CharField(max_length=200)
    text = models.TextField()
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.summury
    
    def get_absolute_url(self):
        return reverse('post_view', args=[str(self.pk)])
    
class PostCommentsModel(models.Model):
    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE
    )
    commenter = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()

    def __str__(self) -> str:
        return str(self.post.pk) + ': ' + self.post.summury

    def get_absolute_url(self):
        return reverse('post_view', args=[str(self.pk)])