from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User


class Blogger(models.Model):
    """Model representing a blogger."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(
        blank=True,
        help_text="Enter a brief biography of the blogger"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular blogger instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of a blogger."""
        return f'{self.last_name}, {self.first_name}'


class Blog(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    description = models.TextField(help_text="Enter the content of the blog post")
    post_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of a blog post."""
        return self.title
    

class Comment(models.Model):
    """Model representing a blog comment."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,  
        blank=True     
    )
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """String representation of a comment."""
        commenter_name = self.commenter.username if self.commenter else "Anonymous"
        return f'Comment by {commenter_name} on {self.blog.title}'