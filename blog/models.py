from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, # redirecting to the custom user model defined in accounts app.
        on_delete=models.CASCADE, # if the user is deleted, all their posts will delete. But here we can also use PROTECT to prevent deletion of user if they have posts.
        related_name='posts'
    )

    def __str__(self):
       return self.title