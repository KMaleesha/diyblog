from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a blog genre (e.g. Science Fiction, French Poetry etc.)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]
        
        
        
class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            unique=True,
                            help_text="Enter the blog's natural language (e.g. English, French, Japanese etc.)")

    def get_absolute_url(self):
        """Returns the url to access a particular language instance."""
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]
        


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
    """Model representing a comment on a blog post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    commenter_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of a comment."""
        return f'Comment by {self.commenter_name} on {self.blog.title}'
