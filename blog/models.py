from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Creates a database to store the blog post's details
#This model uses an imported object called User
#As seen in django documentation: https://docs.djangoproject.com/en/4.1/topics/auth/default/
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #When a user is deleted, on_delete removes their posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    
    # __str__ represents the class objects as a string
    #In this case it returns the post title
    def __str__(self):
        return self.title

    #this tells django how to find the url to a specific post using the post's primary key
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

#Creates a database to store a user's contact details and message
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    # __str__ represents the class objects as a string
    #In this case it returns the email
    def __str__(self):
        return self.email

#Creates a database to store a user's comment and user details
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    #When a user is deleted, on_delete removes their comments
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # __str__ represents the class objects as a string
    #In this case it returns the post title and name
    def __str__(self):
        return self.post.title and self.name

    #this tells django how to find the url to a specific post using the post's primary key
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.post_id})