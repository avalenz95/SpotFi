from django.db import models
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Song(models.Model):
    """ Represents a single wiki page. """
    title = models.CharField(max_length=settings.WIKI_PAGE_TITLE_MAX_LENGTH, unique=True,
                             help_text="Title of your page.")
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               help_text="The user that posted this article.")
    
    

    def __str__(self):
        return self.title

