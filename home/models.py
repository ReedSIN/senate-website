from django.db import models
from mezzanine.core.models import RichText

# Create your models here.

class FeaturedBox(RichText):
    class Meta:
        verbose_name_plural = "Featured Box"

class LeftPanel(RichText):
    class Meta:
        verbose_name_plural = "Left Panel"

class CenterPanel(RichText):
    class Meta:
        verbose_name_plural = "Center Panel"
