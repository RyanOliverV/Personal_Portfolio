from django.db import models
from django.contrib.auth.models import User

#stores users' profile information in the database, such as username and profile picture
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Reference for default.jpg
    #(2020) Male and female symbol. Available at: https://www.vecteezy.com/vector-art/1840645-male-and-female-symbol-human-profile-icon-or-people-icon-man-and-woman-sign-and-symbol-vector
    image = models.ImageField(default='default.jpg', upload_to='static')

    # __str__ represents the class objects as a string
    #In this case it returns the username
    def __str__(self):
        return f'{self.user.username} Profile'