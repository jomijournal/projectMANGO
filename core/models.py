from django.db import models
from django.contrib.auth.models import User


'''
Institution: Holds the data associated with each institution. Institutions will
             be added as new hospitals and libraries register.
'''
class Institution(models.Model):
    name = models.CharField(max_length = 64,
           help_text = 'Name of the institution(e.g. Massachusetts General Hospital).')
    
    location = models.CharField(max_length = 256, help_text = 'Where the institution is located')
    
    IPrange = models.TextField(help_text = 'Range of the IP addresses associated with the institution.')
    
    # necessary?
    pointsOfContact = models.TextField(help_text = 'Librarians or other users who should ' +
                                       'have special access. This will likely include '+
                                       'access to Counter reports.')


'''
User: Holds the data associated with each user registered on the website.
'''
class Account(models.Model):
    # Discuss choices with Bizdev and Editorial
    ACCOUNT_TYPES = (
            (0, 'Other'),
            (1, 'Doctor'),
            (2, 'Resident'),
            (3, 'Medical Student'),
            (4, 'Librarian'),
            (5, 'Attending'),
            (6, 'Premed'),
            (7, 'Veterinarian'),
    )
    user = models.OneToOneField(User)
    
    accountType = models.IntegerField( choices = ACCOUNT_TYPES, default = 0,
                  help_text = 'The account type which affects what a user can do.\
                             This is mostly for JoMI\'s internal records because the\
                             User type already includes a group that we can define.')
    
    institution = models.ForeignKey(Institution,
                  help_text = 'Institution associated with the user.')
    
    # social login ??


'''
Author: Class inherits from User. The Author class additionally
        includes also includes a link to the individual\'s picture, their
        specialty, and their position.
'''
class Author(models.Model):
    
    account = models.ForeignKey(Account)
    
    displayName = models.CharField(max_length = 32, help_text = 'The user\'s nickname.')
    
    image = models.URLField(help_text = 'A link to an image of the author.')
    
    specialty = models.CharField(max_length = 64,
                help_text = 'The author\'s specialty.')
    
    position = models.CharField(max_length = 64,
               help_text = 'The author\'s position.')
