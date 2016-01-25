from django.db import models
from mezzanine.core.models import RichText
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.pages.models import Page

# Create your models here.

class HomePage(models.Model):
    '''
    A page representing the format of the home page
    '''
    featured_box_background = models.ImageField(blank=True,
        help_text="Background image to appear behind feature box.")
    
    featured_box_heading = models.CharField(max_length=200,
                               help_text="The heading of the featured box")
    featured_box_content = models.CharField(max_length=200,
                                  help_text="The text for the featured box")
    featured_box_link = models.CharField(max_length=200,
                                         help_text="The url where the featured box links to")
    featured_box_button = models.CharField(max_length=20,
                                           help_text="The text of the featured box link",
                                           default="Read more")
    left_panel = RichTextField(blank=True, null=True,
                                      help_text="The content for the left panel")
    center_panel = RichTextField(blank=True, null=True,
                                 help_text="The content for the center panel")

    class Meta:
        verbose_name = "Home page"
        verbose_name_plural = "Home pages"
